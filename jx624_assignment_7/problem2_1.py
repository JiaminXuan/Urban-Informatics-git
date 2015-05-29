import sys, csv
import matplotlib.pyplot as plt
from datetime import datetime as dt
import matplotlib.patches as mpatches
hand=[]
times={'NYPD':{},'TLC':{},'DPR':{}}
with open(sys.argv[1]) as f:
	csvread=csv.reader(f)
	header=next(csvread)
	for row in csvread:
		time=dt.strptime(row[1][:10],"%m/%d/%Y")
		agency=row[3]
		if agency in times:
			if time in times[agency]:
				times[agency][time]+=1
			else:
				times[agency][time]=1
color_num=0
color=['r','b','y','pink','g','m','c']
for dep in times:
	time_count=sorted(times[dep].iteritems(), key=lambda x: x[0], reverse=False)
	time,count=zip(*time_count)
	plt.plot(time,count,color=color[color_num])
	red_patch = mpatches.Patch(color=color[color_num], label=dep)
	hand.append(red_patch)
	color_num+=1
plt.ylabel('Volume')
plt.xlabel('Date')
plt.title('Time Series of different agencies') 
plt.legend(handles= hand,loc=2)
plt.show()
	