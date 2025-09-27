public static boolean print(NetcdfFile nc, String command, Writer out, ucar.nc2.util.CancelTask ct)
          throws IOException {
    WantValues showValues = WantValues.none;
    boolean ncml = false;
    boolean strict = false;
    String varNames = null;
    String trueDataset = null;
    String fakeDataset = null;

    if (command != null) {
      StringTokenizer stoke = new StringTokenizer(command);

      while (stoke.hasMoreTokens()) {
        String toke = stoke.nextToken();
        if (toke.equalsIgnoreCase("-help")) {
          out.write(usage);
          out.write('\n');
          return true;
        }
        if (toke.equalsIgnoreCase("-vall"))
          showValues = WantValues.all;
        if (toke.equalsIgnoreCase("-c") && (showValues == WantValues.none))
          showValues = WantValues.coordsOnly;
        if (toke.equalsIgnoreCase("-ncml"))
          ncml = true;
        if (toke.equalsIgnoreCase("-cdl") || toke.equalsIgnoreCase("-strict"))
          strict = true;
        if(toke.equalsIgnoreCase("-v") && stoke.hasMoreTokens())
          varNames = stoke.nextToken();
        if (toke.equalsIgnoreCase("-datasetname") && stoke.hasMoreTokens()) {
          fakeDataset = stoke.nextToken();
          if(fakeDataset.length() == 0) fakeDataset = null;
          if(fakeDataset != null) {
            trueDataset = nc.getLocation();
            nc.setLocation(fakeDataset);
          }
        }
      }
    }

    boolean ok = print(nc, out, showValues, ncml, strict, varNames, ct);
    if(trueDataset != null && fakeDataset != null)
      nc.setLocation(trueDataset);
    return ok;
  }