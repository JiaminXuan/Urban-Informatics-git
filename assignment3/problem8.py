import operator
import csv
import sys
from datetime import datetime, date
ny={}
sf={}
nygeo=[-74.2557,40.4957,-73.6895,40.9176]
sfgeo=[-122.5155,37.7038,-122.3247,37.8545]

with open(sys.argv[1]) as f:
	csvReader=csv.reader(f)
	for row in csvReader:
		if (nygeo[0]<=float(row[2])<=nygeo[2])&(nygeo[1]<=float(row[3])<=nygeo[3]):
			for item in row[4:]:
				if item in ny.keys():
					ny[item]+=1
				else:
					ny[item]=1
		elif (sfgeo[0]<=float(row[2])<=sfgeo[2])&(sfgeo[1]<=float(row[3])<=sfgeo[3]):
			for item in row[4:]:
				if item in sf.keys():
					sf[item]+=1
				else:
					sf[item]=1
x=sorted(ny.iteritems(), key=lambda ny : (-ny[1], ny[0]), reverse=False)
print 'New York:'
for i in range(0,5):
    print str(x[i][0])+', '+str(x[i][1])
x=sorted(sf.iteritems(), key=lambda sf: (-sf[1], sf[0]),reverse=False)
x.sort(key=lambda tup: tup[1],reverse=True)
print 'San Francisco:'
for i in range(0,5):
    print str(x[i][0])+', '+str(x[i][1])