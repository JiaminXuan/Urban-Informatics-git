import csv,sys
from datetime import datetime as dt
from matplotlib import pyplot as plt
applestock=[]
date=[]
with open(sys.argv[1]) as ff:
	f=csv.reader(ff)
	header=next(f)
	for row in f:
		date.append(dt.strptime(row[0],"%Y-%m"))
		applestock.append(float(row[1]))
plt.xticks(rotation=30)
plt.plot(date,applestock,':b.',alpha=0.9)
plt.title('Apple Stock Price')
plt.xlabel('Date')
plt.ylabel('Stock Price')
plt.show()