import csv
import sys
from datetime import datetime, date
import time
name=[]
minDate = datetime.strptime(date.max.isoformat(),"%Y-%m-%d")
maxDate = datetime.strptime(date.min.isoformat(),"%Y-%m-%d")
with open(sys.argv[1]) as f:
	csvReader=csv.reader(f)
	for row in csvReader:
		if row[0] in name:
			pass
		else:
			name.append(row[0])
		creationDateformatted=datetime.strptime(row[1],"%a %b %d %H:%M:%S %Z %Y")
		if creationDateformatted<minDate:
			minDate=creationDateformatted
		if creationDateformatted>maxDate:
			maxDate=creationDateformatted
	print str(len(name))+' users tweeted between '+str(minDate.strftime("%B %d %Y, %H:%M:%S"))+' and '+str(maxDate.strftime("%B %d %Y, %H:%M:%S"))	