from pandas import DataFrame as df
import sys
import numpy
data=df.from_csv(sys.argv[1])
data.sort(['Year of Introduction'],ascending=1,inplace=True)
from matplotlib import pyplot as plt
f, (fares_feb1, ax2) = plt.subplots(1, 2, sharey=False,sharex=True)
fares_feb1.plot(range(len(data)),data['Year of Introduction'],'--b.')
fares_feb1.set_title('Year of introduction of processors')
fares_feb1.set_ylabel('Year of introduction')
fares_feb1.set_xlabel('Processors')
fares_feb1.set_xticklabels(data.index)
fares_feb1.set_xticks(range(len(data)))
ax2.plot(range(len(data)),numpy.log10(data['Transistors']),'--r.')
ax2.set_title('Number of transistors of processors')
ax2.set_ylabel('Number of transistors (log10)')
ax2.set_xlabel('Processors')
plt.setp(fares_feb1.xaxis.get_majorticklabels(), rotation=90 )
plt.setp(ax2.xaxis.get_majorticklabels(), rotation=90 )
plt.show()
