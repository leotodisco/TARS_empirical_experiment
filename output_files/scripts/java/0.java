private String processQueryElements(String urlToFilter) {
        try {
            // Handle illegal characters by making a url first
            // this will clean illegal characters like |
            URL url = new URL(urlToFilter);

            String query = url.getQuery();
            String path = url.getPath();

            // check if the last element of the path contains parameters
            // if so convert them to query elements
            if (path.contains(";")) {
                String[] pathElements = path.split("/");
                String last = pathElements[pathElements.length - 1];
                // replace last value by part without params
                int semicolon = last.indexOf(";");
                if (semicolon != -1) {
                    pathElements[pathElements.length - 1] = last.substring(0,
                            semicolon);
                    String params = last.substring(semicolon + 1).replaceAll(
                            ";", "&");
                    if (query == null) {
                        query = params;
                    } else {
                        query += "&" + params;
                    }
                    // rebuild the path
                    StringBuilder newPath = new StringBuilder();
                    for (String p : pathElements) {
                        if (StringUtils.isNotBlank(p)) {
                            newPath.append("/").append(p);
                        }
                    }
                    path = newPath.toString();
                }
            }

            if (StringUtils.isEmpty(query)) {
                return urlToFilter;
            }

            List<NameValuePair> pairs = URLEncodedUtils.parse(query,
                    StandardCharsets.UTF_8);
            Iterator<NameValuePair> pairsIterator = pairs.iterator();
            while (pairsIterator.hasNext()) {
                NameValuePair param = pairsIterator.next();
                if (queryElementsToRemove.contains(param.getName())) {
                    pairsIterator.remove();
                } else if (removeHashes && param.getValue() != null) {
                    Matcher m = thirtytwobithash.matcher(param.getValue());
                    if (m.matches()) {
                        pairsIterator.remove();
                    }
                }
            }

            StringBuilder newFile = new StringBuilder();
            if (StringUtils.isNotBlank(path)) {
                newFile.append(path);
            }
            if (!pairs.isEmpty()) {
                Collections.sort(pairs, comp);
                String newQueryString = URLEncodedUtils.format(pairs,
                        StandardCharsets.UTF_8);
                newFile.append('?').append(newQueryString);
            }
            if (url.getRef() != null) {
                newFile.append('#').append(url.getRef());
            }

            return new URL(url.getProtocol(), url.getHost(), url.getPort(),
                    newFile.toString()).toString();
        } catch (MalformedURLException e) {
            LOG.warn("Invalid urlToFilter {}. {}", urlToFilter, e);
            return null;
        }
    }