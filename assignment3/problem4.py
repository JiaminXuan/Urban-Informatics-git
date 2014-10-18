import operator
import csv
import sys
from datetime import datetime, date
hashtag1={}
with open(sys.argv[1]) as f:
	csvReader=csv.reader(f)
	for row in csvReader:
		for item in row[4:]:
			if item in hashtag1.keys():
				hashtag1[item]+=1
			else:
				hashtag1[item]=1
x=sorted(hashtag1.iteritems(), key=operator.itemgetter(0),reverse=False)
x.sort(key=lambda tup: tup[1],reverse=True)
for i in range(0,10):
    print str(x[i][0])+', '+str(x[i][1])
	