#!/usr/bin/python

from collections import OrderedDict

roman = OrderedDict([('I',1),('V',5),('X',10),('L',50),('C',100),('D',500),('M',1000)])
rules = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']
bads = [i+j for i in roman.keys() for j in roman.keys() 
        if i+j not in rules and roman[j] > roman[i]]
bads += ['IIII', 'VVVV', 'XXXX', 'LLLL', 'CCCC', 'DDDD']

ints = [(1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),(100,'C'),(90,'XC'),
        (50,'L'),(40,'XL'),(10,'X'),(9,'X'),(5,'V'),(4,'IV'),(1,'I')]

def r2d(num):
	if not set(num).issubset(roman.keys()) or [i for i in bads if i in num]: return None
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
	cur = num
	for i in ints:
		val += cur/i[0]*i[1]
		cur %= i[0]
	return val
	