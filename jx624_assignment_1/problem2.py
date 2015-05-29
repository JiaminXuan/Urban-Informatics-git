from pandas import DataFrame
import sys

rawdata=DataFrame.from_csv(sys.argv[1])
complain_type_list=list(rawdata.iloc[:,4])
counter_set=set(complain_type_list)

for words in counter_set:
	print str(words)+' with '+str(complain_type_list.count(words))+' complaints'