#!/usr/bin/python

from collections import OrderedDict

roman = OrderedDict([('I',1),('V',5),('X',10),('L',50),('C',100),('D',500),('M',1000)])
rules = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']
bads = [i+j for i in roman.keys() for j in roman.keys() 
        if i+j not in rules and roman[j] > roman[i]]
bads += [i*4 for i in roman.keys()][:-1]

ints = [(1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),(100,'C'),(90,'XC'),
        (50,'L'),(40,'XL'),(10,'X'),(9,'X'),(5,'V'),(4,'IV'),(1,'I')]

def r2d(num):
	if not set(num).issubset(roman.keys()) or [i for i in bads if i in num]: return None
	if '(' in num or ')' in num:
		if '(' in num and ')' in num:
			return 1000 
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
	if num/5000: 
		return '(' + d2r((num - num%5000)/1000) + ')' + d2r(num%5000)
	else:
		val = ''
		cur = num
		for i in ints:
			val += cur/i[0]*i[1]
			cur %= i[0]
		return val
	
