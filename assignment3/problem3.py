import csv
import sys
from datetime import datetime, date
hashtag1=[]
hashtag2=[]
output=[]
with open(sys.argv[1]) as f:
	csvReader=csv.reader(f)
	for row in csvReader:
		for item in row[4:]:
			if item in hashtag1:
				pass
			else:
				hashtag1.append(item)
with open(sys.argv[2]) as f:
	csvReader=csv.reader(f)
	for row in csvReader:
		for item in row[4:]:
			if item in hashtag2:
				pass
			else:
				hashtag2.append(item)
for hashlist in hashtag1:
	if hashlist in hashtag2:
		output.append(hashlist[1:])
for item in sorted(output):
	print '#'+item
