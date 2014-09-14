from pandas import DataFrame
import csv,sys
from datetime import datetime, date
mylist=[]
with open(sys.argv[1]) as f:
	csvReader=csv.reader(f)
	next(csvReader,None)
	for row in csvReader:
		creationDateformatted=datetime.strptime(row[1],"%m/%d/%Y %I:%M:%S %p").date().weekday()
		mylist.append(creationDateformatted)
	myset=set(mylist)
	dictionary_weekday={0:'Monday',1:'Tuesday',2:'Wednesday',3:'Thursday',4:'Friday',5:'Saturday',6:'Sunday'}
	for days in range(7):
		print str(dictionary_weekday[days])+' == '+str(mylist.count(days))
