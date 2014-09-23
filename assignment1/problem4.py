from pandas import DataFrame
import sys

rawdata=DataFrame.from_csv(sys.argv[1])
complain_type_raw=list(rawdata.iloc[:,4])
counter_set=set(complain_type_raw)
complain_type_list=[]
numbers_list=[]
for words in counter_set:
	complain_type_list.append(words)
	numbers_list.append(complain_type_raw.count(words))
	complaint_number=DataFrame({'complain_type':complain_type_list,'numbers':numbers_list})
sorted_C_N=complaint_number.sort(['numbers','complain_type'],ascending=[0,1])

for i in range(int(sys.argv[2])):
	print str(sorted_C_N.iloc[i,0])+' with '+str(sorted_C_N.iloc[i,1])+' complaints'
