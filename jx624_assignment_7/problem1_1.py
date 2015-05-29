import sys, csv
import matplotlib.pyplot as plt
import numpy as np
agencylist=['NYPD','DOT','DOB','TLC','DPR']
with open(sys.argv[1]) as f:
	csvread=csv.reader(f)
	agencyCount={}
	for row in csvread:
		agency = row[3]
		if agency in agencylist:
			count = agencyCount.setdefault(agency, 0)
			agencyCount[agency] = count + 1

plt.bar(np.arange(0,5,1),agencyCount.values(),alpha=0.5,color=['r','b','y','pink','g'],linewidth=0,align='center')
plt.xticks(np.arange(0,5,1),agencylist)
plt.ylabel('Volume')
plt.xlabel('Agency')
plt.title('Volume of Complaints')
plt.show()