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

plt.plot(date,applestock,':b.',alpha=0.8)
plt.axhline(y=applestock[-1], color='b',linestyle='--',alpha=0.5)
plt.plot(date,msstock,':r.',alpha=0.8)
plt.axhline(y=msstock[-1], color='r',linestyle='--',alpha=0.5)
plt.xticks(rotation=30)
plt.title('Apple ~ Microsoft Stock Price')
plt.xlabel('Date')
plt.ylabel('Stock Price')
plt.show()