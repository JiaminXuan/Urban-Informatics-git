from pandas import DataFrame as df
import pandas as pd
import sys
from datetime import datetime
from matplotlib import pyplot as plt
data=df.from_csv(sys.argv[1],index_col='Unique Key',parse_dates=True,infer_datetime_format=True)
data['Created Date']=map(lambda x: datetime.strptime(x[:10],"%m/%d/%Y"),data['Created Date'])
ts=data[['Created Date','Borough']].groupby(by=['Created Date','Borough']).size().unstack()[['BRONX','BROOKLYN','MANHATTAN','QUEENS','STATEN ISLAND']]
ts.plot(label='Series',figsize=(22,11),x_compat=True)
plt.show()