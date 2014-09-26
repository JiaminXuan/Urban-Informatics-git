import csv
import sys
hashtag1={}
hashtag2={}
with open(sys.argv[1]) as f:
	csvReader=csv.reader(f)
	for row in csvReader:
		for item in row[4:]:
			if item in hashtag1:
				pass
			else:
				hashtag1[item]=None
with open(sys.argv[2]) as f:
	csvReader=csv.reader(f)
	for row in csvReader:
		for item in row[4:]:
			if item in hashtag1:
				hashtag2[item]=item[1:]
output=sorted(hashtag2.values())
for item in output:
	print '#'+item
