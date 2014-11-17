#!/usr/bin/python

import re
from datetime import datetime
from collections import defaultdict

timeRE = re.compile(r'(?P<dt>[0-9]{1,2}-[0-9]{1,2}-[0-9]{4}): (?P<start>[0-9][0-9]:[0-9][0-9] [A|P]M) to (?P<end>[0-9][0-9]:[0-9][0-9] [A|P]M) -- (?P<act>[A-Za-z ]*)')
format = '%m-%d-%Y %I:%M %p'
sched, timeTot = defaultdict(list),defaultdict(int)

inputlist = open('input.txt','r').readlines()

for i in inputlist:
	m = timeRE.match(i)
	date = datetime.strptime(m.group('dt'),format[:8])
	start = datetime.strptime(m.group('dt')+' '+m.group('start'),format)
	end = datetime.strptime(m.group('dt')+' '+m.group('end'),format)
	duration = int((end - start).total_seconds())/60
	act = m.group('act')
	
	sched[date].append((start,end,duration,act))
	timeTot[act] += duration

def findMaxGap(inp):
	inp = sorted(inp)
	maxgap = 0
	nitems = len(inp)

	for i,j in enumerate(inp):
		if i+1 == nitems: break
		gap = int((inp[i+1][0] - j[1]).total_seconds())/60
		if gap > maxgap: 
			maxgap = gap
			start = j[1]
			end = inp[i+1][0]

	return (start,end,maxgap,'reddit')

for day in sorted(sched):
	print(day.strftime('Schedule for %A, %d %B %Y:'))
	for i in sorted(sched[day]):
		print('\t%s - %s : %s (%s min)' % (i[0].strftime(format[-8:]),i[1].strftime(format[-8:]),i[3],i[2]))

print('activity breakdown')
total = sum([timeTot[i] for i in timeTot])
for act in timeTot: 
	print('\t%s: %i (%5.2f%%)' % (act, timeTot[act], timeTot[act]*100/float(total)))
