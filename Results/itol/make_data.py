#!/usr/bin/python

import io
import sys

fname = sys.argv[1]
f = open(fname)

name_count = {}
vals = {}
for line in f:
	s = line.split() #splits results and name
	name = s[0] #gets name
	val = s[1]
	if name in name_count:
		name_count[name] += 1
		vals[name].append(val)
	else:
		name_count[name] = 1
		vals[name] = [val]
f.close()

for n in name_count:
	if name_count[n] < 2:
		vals[n].append(0)

for n in vals:
	print "%s\t%s" % (n,vals[n])
