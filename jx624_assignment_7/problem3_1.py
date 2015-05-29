import csv,sys
from pandas import DataFrame as df
import pandas
import matplotlib.pyplot as plt
zipcode={}
with open (sys.argv[1]) as f1:
	csvread=csv.reader(f1)
	header=next(csvread)
	for row in csvread:
		# print '...'+row[8].strip()[:5]+'...'
		try:
			code=int(row[8].strip()[:5])
			if code in zipcode:
				zipcode[code]+=1
			else:
				zipcode[code]=1
		except:
			pass
zipcode_s=df(zipcode.values(),index=zipcode.keys())
z311={}
with open (sys.argv[2]) as f1:
	csvread=csv.reader(f1)
	header=next(csvread)
	for row in csvread:
		try:
			code=int(row[0].strip()[:5])
			z311[code]=int(row[1])
		except:
			pass
zipcode_311=df(z311.values(),index=z311.keys())
data=pandas.merge(zipcode_s,zipcode_311,how='inner',left_index=True, right_index=True)
plt.scatter(data['0_y'],data['0_x'],alpha=0.3)

plt.ylabel('Volume')
plt.xlabel('population')
plt.title('The scatter of different zipcode') 
plt.show()


