import csv
import sys
from datetime import datetime, date
counter=0
minDate = datetime.strptime(date.max.isoformat(),"%Y-%m-%d")
maxDate = datetime.strptime(date.min.isoformat(),"%Y-%m-%d")
with open(sys.argv[1]) as f:
	csvReader=csv.reader(f)
	for row in csvReader:
		counter+=1
		creationDateformatted=datetime.strptime(row[1],"%a %b %d %H:%M:%S %Z %Y")
		if creationDateformatted<minDate:
			minDate=creationDateformatted
		if creationDateformatted>maxDate:
			maxDate=creationDateformatted
	print 'There were '+str(counter)+' tweets between '+str(minDate.strftime("%B %d %Y, %H:%M:%S"))+' and '+str(maxDate.strftime("%B %d %Y, %H:%M:%S"))	


