import csv,sys
from datetime import datetime as dt
from matplotlib import pyplot as plt
import math
import numpy as np
from pandas import DataFrame as df

date=[]
with open(sys.argv[1]) as ff:
	f=csv.reader(ff)
	header=next(f)
	for row in f:
		ds=dt.strptime(row[0],"%Y-%m-%d %H:%M:%S")
		date.append(ds.year*1000000+ds.month*10000+ds.day*100+ds.hour*1)
# f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)

aa=int(len(date)/(2*np.subtract(*np.percentile(date, [75, 25]))*len(date)**(-1.0/3)))
plt.hist(date,bins=aa)
plt.ticklabel_format(style='plain')
plt.show()
