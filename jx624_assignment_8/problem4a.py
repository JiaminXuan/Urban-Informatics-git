import matplotlib
from matplotlib import pyplot as plt
from pandas.tools.plotting import scatter_matrix
import csv,sys
from pandas import DataFrame
def set_column_sequence(dataframe, seq):
    cols = seq[:]
    for x in dataframe.columns:
        if x not in cols:
            cols.append(x)
    return dataframe[cols]
data={'A':[],'B':[],'C':[],'D':[]}
with open(sys.argv[1]) as ff:
	f=csv.reader(ff)
	header=next(f)
	for row in f:
		data['A'].append(float(row[0]))
		data['B'].append(float(row[1]))
		data['C'].append(float(row[2]))
		data['D'].append(float(row[3]))		
df = DataFrame.from_dict(data)
dfo=set_column_sequence(df, ['A','C','D','B'])
a=scatter_matrix(dfo, alpha=0.5, figsize=(16, 16), diagonal='kde')
plt.show()
print dfo