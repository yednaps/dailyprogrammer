#!/usr/bin/python

from collections import OrderedDict

roman = OrderedDict([('I',1),('V',5),('X',10),('L',50),('C',100),('D',500),('M',1000)])

def r2d(num):
	if not set(num).issubset(roman.keys()): return None
	val = 0
	for i,d in enumerate(num):
		if i + 1 < len(num):
			if roman.keys().index(d) < roman.keys().index(num[i+1]):
				val -= roman[d]
			else:
				val += roman[d]
		else: val += roman[d]
	return val

def d2r(num):
	val = ''
	if 
	valnum/