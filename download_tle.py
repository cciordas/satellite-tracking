#! /usr/bin/env python

import urllib2
URL = "http://www.celestrak.com/NORAD/elements/amateur.txt"


whandle = urllib2.urlopen(URL)
fhandle = open("/Users/cciordas/projects/satellite_tracking/tle_amateur.txt", "w")                                       # <-- this is where we save it
fhandle.write(whandle.read())
fhandle.close()
