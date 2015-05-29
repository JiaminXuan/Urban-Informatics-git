import csv
import sys
from datetime import datetime, date

def printtotalnum(filedirectory):
	with open(filedirectory) as f:
		counter=0
		csvReader=csv.reader(f)
		header=next(csvReader)
		minDate = datetime.strptime(date.max.isoformat(),"%Y-%m-%d")
		maxDate = datetime.strptime(date.min.isoformat(),"%Y-%m-%d")
		for row in csvReader:
			counter+=1
			complainType=row[5]
			creationDateformatted=datetime.strptime(row[1],"%m/%d/%Y %I:%M:%S %p")
			#print complainType+' happened at '+str(creationDateformatted)
			#"%m/%d/%Y %I:%M:%S %p"
			if creationDateformatted<minDate:
				minDate=creationDateformatted
			if creationDateformatted>maxDate:
				maxDate=creationDateformatted
		print str(counter)+' complaints between '+str(minDate.strftime("%m/%d/%Y %H:%M:%S"))+' and '+str(maxDate.strftime("%m/%d/%Y %H:%M:%S"))	

filepath=sys.argv[1]
printtotalnum(filepath)	
