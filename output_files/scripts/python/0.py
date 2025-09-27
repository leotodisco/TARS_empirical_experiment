def attendee(request, form, user_id=None):
    ''' Returns a list of all manifested attendees if no attendee is specified,
    else displays the attendee manifest. '''

    if user_id is None and form.cleaned_data["user"] is not None:
        user_id = form.cleaned_data["user"]

    if user_id is None:
        return attendee_list(request)

    attendee = people.Attendee.objects.get(user__id=user_id)
    name = attendee.attendeeprofilebase.attendee_name()

    reports = []

    profile_data = []
    try:
        profile = people.AttendeeProfileBase.objects.get_subclass(
            attendee=attendee
        )
        fields = profile._meta.get_fields()
    except people.AttendeeProfileBase.DoesNotExist:
        fields = []

    exclude = set(["attendeeprofilebase_ptr", "id"])
    for field in fields:
        if field.name in exclude:
            # Not actually important
            continue
        if not hasattr(field, "verbose_name"):
            continue  # Not a publicly visible field
        value = getattr(profile, field.name)

        if isinstance(field, models.ManyToManyField):
            value = ", ".join(str(i) for i in value.all())

        profile_data.append((field.verbose_name, value))

    cart = CartController.for_user(attendee.user)
    reservation = cart.cart.reservation_duration + cart.cart.time_last_updated
    profile_data.append(("Current cart reserved until", reservation))

    reports.append(ListReport("Profile", ["", ""], profile_data))

    links = []
    links.append((
        reverse(views.badge, args=[user_id]),
        "View badge",
    ))
    links.append((
        reverse(views.amend_registration, args=[user_id]),
        "Amend current cart",
    ))
    links.append((
        reverse(views.extend_reservation, args=[user_id]),
        "Extend reservation",
    ))

    reports.append(Links("Actions for " + name, links))

    # Paid and pending  products
    ic = ItemController(attendee.user)
    reports.append(ListReport(
        "Paid Products",
        ["Product", "Quantity"],
        [(pq.product, pq.quantity) for pq in ic.items_purchased()],
    ))
    reports.append(ListReport(
        "Unpaid Products",
        ["Product", "Quantity"],
        [(pq.product, pq.quantity) for pq in ic.items_pending()],
    ))

    # Invoices
    invoices = commerce.Invoice.objects.filter(
        user=attendee.user,
    )
    reports.append(QuerysetReport(
        "Invoices",
        ["id", "get_status_display", "value"],
        invoices,
        headings=["Invoice ID", "Status", "Value"],
        link_view=views.invoice,
    ))

    # Credit Notes
    credit_notes = commerce.CreditNote.objects.filter(
        invoice__user=attendee.user,
    ).select_related("invoice", "creditnoteapplication", "creditnoterefund")

    reports.append(QuerysetReport(
        "Credit Notes",
        ["id", "status", "value"],
        credit_notes,
        link_view=views.credit_note,
    ))

    # All payments
    payments = commerce.PaymentBase.objects.filter(
        invoice__user=attendee.user,
    ).select_related("invoice")

    reports.append(QuerysetReport(
        "Payments",
        ["invoice__id", "id", "reference", "amount"],
        payments,
        link_view=views.invoice,
    ))

    return reports