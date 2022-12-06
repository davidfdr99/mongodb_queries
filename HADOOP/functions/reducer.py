#!/usr/bin/env python

import sys

Total = 0
oldKey = None

for line in sys.stdin:

	#data=line.strip().split("\t")
	data=line.strip()	

	thisKey = data
	if oldKey and oldKey != thisKey:
		print "{0}\t{1}".format(oldKey, Total)
		Total = 0

	oldKey = thisKey
	Total += 1

if oldKey != None:
	print oldKey, "\t", Total
