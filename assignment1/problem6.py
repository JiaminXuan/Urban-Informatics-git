import sys
from pandas import DataFrame as df
zip_code=[]
count_zip=[]
rawdata=df.from_csv(sys.argv[1]).sort('Incident Zip')
Department=rawdata['Agency']
for item in sorted(set(Department)):
	print item,
	for i in range(len(Department)):
		if Department.iloc[i]==item:
			print str(rawdata.iloc[i,6]),
			zip_code.append(rawdata.iloc[i,6])
	countnum=0
	for unique_zip in set(zip_code):		
		if zip_code.count(unique_zip)>countnum:
			countnum=zip_code.count(unique_zip)
	print countnum
