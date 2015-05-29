import sys, csv
import matplotlib.pyplot as plt
from datetime import datetime as dt
import matplotlib.patches as mpatches
hand=[]
times={}
names={}
k=int(sys.argv[2])
with open(sys.argv[1]) as f:
	csvread=csv.reader(f)
	header=next(csvread)
	for row in csvread:
		count=0
		time=dt.strptime(row[1][:10],"%m/%d/%Y").weekday()
		agency=row[3]
		if agency not in times:
			times[agency]={}
			names[agency]=0
		if time in times[agency]:
			times[agency][time]+=1
		else:
			times[agency][time]=1
		names[agency]+=1
name_list=sorted(names.iteritems(), key=lambda x: x[1], reverse=True)
if k> len(name_list):k=len(name_list)
print k
color_num=0
color=['r','b','y','pink','g','m','c']
for dep in name_list[:k]:
	time_count=sorted(times[dep[0]].iteritems(), key=lambda x: x[0], reverse=False)
	time,count=zip(*time_count)
	plt.plot(time,count,color=color[color_num],alpha=0.5)
	red_patch = mpatches.Patch(color=color[color_num], label=dep[0])
	hand.append(red_patch)
	color_num=(color_num+1)%7
plt.ylabel('Volume')
plt.xlabel('Date')
plt.title('Time Series of different agencies') 
plt.legend(handles= hand,loc=2)
plt.show()
# 	