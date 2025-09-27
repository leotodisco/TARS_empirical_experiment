@Override
  public FileCacheable acquire(FileFactory factory, Object hashKey, DatasetUrl location,
                               int buffer_size, CancelTask cancelTask, Object spiObject) throws IOException {

    if (null == hashKey) hashKey = location.trueurl;
    if (null == hashKey) throw new IllegalArgumentException();

    Tracker t = null;
    if (trackAll) {
      t = new Tracker(hashKey);
      Tracker prev = track.putIfAbsent(hashKey, t);
      if (prev != null) t = prev;
    }

    FileCacheable ncfile = acquireCacheOnly(hashKey);
    if (ncfile != null) {
      hits.incrementAndGet();
      if (t != null) t.hit++;
      return ncfile;
    }
    miss.incrementAndGet();
    if (t != null) t.miss++;

    // open the file
    ncfile = factory.open(location, buffer_size, cancelTask, spiObject);
    if (cacheLog.isDebugEnabled())
      cacheLog.debug("FileCacheARC " + name + " acquire " + hashKey + " " + ncfile.getLocation());
    if (debugPrint) System.out.println("  FileCacheARC " + name + " acquire " + hashKey + " " + ncfile.getLocation());

    // user may have canceled
    if ((cancelTask != null) && (cancelTask.isCancel())) {
      if (ncfile != null) ncfile.close();
      return null;
    }

    if (disabled.get()) return ncfile;

    addToCache(hashKey, ncfile);

    return ncfile;
  }