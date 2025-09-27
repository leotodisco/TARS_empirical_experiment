public void
    handleRequest(HttpServletRequest req, HttpServletResponse res)
            throws IOException
    {
        DapLog.debug("doGet(): User-Agent = " + req.getHeader("User-Agent"));
        if(!this.initialized) initialize();
        DapRequest daprequest = getRequestState(req, res);
        String url = daprequest.getOriginalURL();
        StringBuilder info = new StringBuilder("doGet():");
        info.append(" dataset = ");
        info.append(" url = ");
        info.append(url);
        if(DEBUG) {
            System.err.println("DAP4 Servlet: processing url: " + daprequest.getOriginalURL());
        }
        DapContext dapcxt = new DapContext();
        // Add entries to the context
        dapcxt.put(HttpServletRequest.class, req);
        dapcxt.put(HttpServletResponse.class, res);
        dapcxt.put(DapRequest.class, daprequest);

        ByteOrder order = daprequest.getOrder();
        ChecksumMode checksummode = daprequest.getChecksumMode();
        dapcxt.put(Dap4Util.DAP4ENDIANTAG, order);
        dapcxt.put(Dap4Util.DAP4CSUMTAG, checksummode);
        // Transfer all other queries
        Map<String, String> queries = daprequest.getQueries();
        for(Map.Entry<String, String> entry : queries.entrySet()) {
            if(dapcxt.get(entry.getKey()) == null) {
                dapcxt.put(entry.getKey(), entry.getValue());
            }
        }

        if(url.endsWith(FAVICON)) {
            doFavicon(FAVICON, dapcxt);
            return;
        }

        String datasetpath = DapUtil.nullify(DapUtil.canonicalpath(daprequest.getDataset()));
        try {
            if(datasetpath == null) {
                // This is the case where a request was made without a dataset;
                // According to the spec, I think we should return the
                // services/capabilities document
                doCapabilities(daprequest, dapcxt);
            } else {
                RequestMode mode = daprequest.getMode();
                if(mode == null)
                    throw new DapException("Unrecognized request extension")
                            .setCode(HttpServletResponse.SC_BAD_REQUEST);
                switch (mode) {
                case DMR:
                    doDMR(daprequest, dapcxt);
                    break;
                case DAP:
                    doData(daprequest, dapcxt);
                    break;
                case DSR:
                    doDSR(daprequest, dapcxt);
                    break;
                default:
                    throw new DapException("Unrecognized request extension")
                            .setCode(HttpServletResponse.SC_BAD_REQUEST);
                }
            }
        } catch (Throwable t) {
            t.printStackTrace();
            int code = HttpServletResponse.SC_BAD_REQUEST;
            if(t instanceof DapException) {
                DapException e = (DapException) t;
                code = e.getCode();
                if(code <= 0)
                    code = DapCodes.SC_BAD_REQUEST;
                e.setCode(code);
            } else if(t instanceof FileNotFoundException)
                code = DapCodes.SC_NOT_FOUND;
            else if(t instanceof UnsupportedOperationException)
                code = DapCodes.SC_FORBIDDEN;
            else if(t instanceof MalformedURLException)
                code = DapCodes.SC_NOT_FOUND;
            else if(t instanceof IOException)
                code = DapCodes.SC_BAD_REQUEST;
            else
                code = DapCodes.SC_INTERNAL_SERVER_ERROR;
            senderror(daprequest, code, t);
        }//catch
    }