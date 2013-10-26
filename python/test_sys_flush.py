#!/usr/bin/env python
#-*- coding: utf-8 -*-

# subhodeep.moitra@gmail.com

"""
Tests the use of sys.stdout.flush
"""


import sys
import time

for i in range(10):
    sys.stdout.write("\r%d" % i)
    time.sleep(0.1)
    sys.stdout.flush()

print
print("\r".join(map(str, range(5))))


for i in xrange(3):
    print "Hello%s" % i

for i in range(5):
    print i
