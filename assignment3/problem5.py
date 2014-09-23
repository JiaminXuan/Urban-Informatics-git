import csv
import sys
from datetime import datetime, date
hashtag1={}
with open(sys.argv[1]) as f:
	csvReader=csv.reader(f)
	for row in csvReader:
		creationDateformatted=datetime.strptime(row[1],"%a %b %d %H:%M:%S %Z %Y")
		if creationDateformatted in hashtag1.keys():
			hashtag1[creationDateformatted]+=1
		else:
			hashtag1[creationDateformatted]=1
import operator
output=max(hashtag1.iteritems(), key=operator.itemgetter(1))
print str(output[0].strftime("%B %d %Y, %H:%M:%S"))+' with '+str(output[1])+' tweets'