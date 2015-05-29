import csv,os,sys
import matplotlib.pyplot as plt
k=int(sys.argv[2])
color=['r','b','y','pink','g','m','c']
with open(sys.argv[1]) as f:
	csvread=csv.reader(f)
	header=next(csvread)
	agencyCount={}
	for row in csvread:
		agency = row[3]
		count = agencyCount.setdefault(agency, 0)
		agencyCount[agency] = count + 1
sorted_agency_count=sorted(agencyCount.iteritems(), key=lambda x: (-x[1], x[0]), reverse=False)
if k>len(sorted_agency_count): k=len(sorted_agency_count)
kTop=sorted_agency_count[:k]
volumnlist=[]
for i in kTop:
	volumnlist.append(i[1])
namelist=[]
for i in kTop:
	namelist.append(i[0])
colorlist=[]
for i in xrange(k):
	p=(i)%5
	colorlist.append(color[p])
plt.bar(range(k),volumnlist,color=colorlist,linewidth=0,align='center',alpha=0.5)
plt.xticks(range(k),namelist)
plt.ylabel('Volume')
plt.xlabel('Agency')
plt.title('Volume of Complaints')
plt.show()