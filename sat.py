#! /usr/bin/env python

#import numpy as np
import pylab as plt
import ephem
import datetime

# load satellite TLE data
l1 = "OSCAR 7 (AO-7)"
l2 = "1 07530U 74089B   12276.56353410 -.00000027  00000-0  10000-3 0  4953"
l3 = "2 07530 101.4117 269.6609 0012151  72.2029 288.0376 12.53591691733506"
oscar = ephem.readtle(l1, l2, l3)

observer = ephem.Observer()
observer.lon = ephem.degrees('-74.070653')
observer.lat = ephem.degrees('40.68866')

oscar.compute(observer)
print oscar.ra, oscar.dec
print oscar.rise_time, oscar.transit_time, oscar.set_time

