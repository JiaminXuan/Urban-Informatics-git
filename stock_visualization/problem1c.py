import csv,sys
from datetime import datetime as dt
from matplotlib import pyplot as plt
applestock=[]
msstock=[]
date=[]
with open(sys.argv[1]) as ff:
	f=csv.reader(ff)
	header=next(f)
	for row in f:
		date.append(dt.strptime(row[0],"%Y-%m"))
		applestock.append(float(row[1]))
		msstock.append(float(row[2]))
f, (ax1, ax2) = plt.subplots(1, 2, sharey=True,sharex=True)
plt.xticks(rotation=30)
ax1.plot(date,applestock,':b.',alpha=0.8)
ax1.axhline(y=applestock[-1], color='b',linestyle='--',alpha=0.5)
ax1.set_title('Apple Stock Price')
plt.setp(ax1.xaxis.get_majorticklabels(), rotation=30 )
ax1.set_xlabel('Date')
ax1.set_ylabel('Stock Price')
ax2.plot(date,msstock,':r.',alpha=0.8)
ax2.axhline(y=msstock[-1], color='r',linestyle='--',alpha=0.5)
plt.title('Microsoft Stock Price')
plt.xlabel('Date')
plt.ylabel('Stock Price')
plt.show()