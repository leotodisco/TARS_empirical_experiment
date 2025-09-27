def subscribe(self, subject,
                  queue="",
                  cb=None,
                  future=None,
                  max_msgs=0,
                  is_async=False,
                  pending_msgs_limit=DEFAULT_SUB_PENDING_MSGS_LIMIT,
                  pending_bytes_limit=DEFAULT_SUB_PENDING_BYTES_LIMIT,
                  ):
        """
        Takes a subject string and optional queue string to send a SUB cmd,
        and a callback which to which messages (Msg) will be dispatched to
        be processed sequentially by default.
        """
        if subject == "":
            raise ErrBadSubject

        if self.is_closed:
            raise ErrConnectionClosed

        if self.is_draining:
            raise ErrConnectionDraining

        sub = Subscription(subject=subject,
                           queue=queue,
                           max_msgs=max_msgs,
                           is_async=is_async,
                           )
        if cb is not None:
            if asyncio.iscoroutinefunction(cb):
                sub.coro = cb
            elif sub.is_async:
                raise NatsError(
                    "nats: must use coroutine for async subscriptions")
            else:
                # NOTE: Consider to deprecate this eventually, it should always
                # be coroutines otherwise they could affect the single thread,
                # for now still allow to be flexible.
                sub.cb = cb

            sub.pending_msgs_limit = pending_msgs_limit
            sub.pending_bytes_limit = pending_bytes_limit
            sub.pending_queue = asyncio.Queue(
                maxsize=pending_msgs_limit,
                loop=self._loop,
                )

            # Close the delivery coroutine over the sub and error handler
            # instead of having subscription type hold over state of the conn.
            err_cb = self._error_cb

            @asyncio.coroutine
            def wait_for_msgs():
                nonlocal sub
                nonlocal err_cb

                while True:
                    try:
                        msg = yield from sub.pending_queue.get()
                        sub.pending_size -= len(msg.data)

                        try:
                            # Invoke depending of type of handler.
                            if sub.coro is not None:
                                if sub.is_async:
                                    # NOTE: Deprecate this usage in a next release,
                                    # the handler implementation ought to decide
                                    # the concurrency level at which the messages
                                    # should be processed.
                                    self._loop.create_task(sub.coro(msg))
                                else:
                                    yield from sub.coro(msg)
                            elif sub.cb is not None:
                                if sub.is_async:
                                    raise NatsError(
                                        "nats: must use coroutine for async subscriptions")
                                else:
                                    # Schedule regular callbacks to be processed sequentially.
                                    self._loop.call_soon(sub.cb, msg)
                        except asyncio.CancelledError:
                            # In case the coroutine handler gets cancelled
                            # then stop task loop and return.
                            break
                        except Exception as e:
                            # All errors from calling a handler
                            # are async errors.
                            if err_cb is not None:
                                yield from err_cb(e)

                    except asyncio.CancelledError:
                        break

            # Start task for each subscription, it should be cancelled
            # on both unsubscribe and closing as well.
            sub.wait_for_msgs_task = self._loop.create_task(
                wait_for_msgs())

        elif future is not None:
            # Used to handle the single response from a request.
            sub.future = future
        else:
            raise NatsError("nats: invalid subscription type")

        self._ssid += 1
        ssid = self._ssid
        self._subs[ssid] = sub
        yield from self._subscribe(sub, ssid)
        return ssid