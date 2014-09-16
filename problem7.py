import sys,csv,operator
sumnum=[]
final_output_dict={}
file1=open(sys.argv[1])
file2=open(sys.argv[2])
csvReader1=csv.reader(file1)
next(csvReader1,None)
csvReader2=csv.reader(file2)
next(csvReader2,None)
incidentzip=[]
zipcode={}
for item in csvReader1:	
	incidentzip.append(item[7])
for code in csvReader2:
	zipcode[code[0]]=code[1]
for item in incidentzip:
	for code in zipcode:
		if item==code:
			sumnum.append(zipcode[code])
for item in set(sumnum):
	final_output_dict[item]=sumnum.count(item)

final_sorted_output=sorted(final_output_dict.iteritems(), key=operator.itemgetter(1),reverse = True)
for borough,number in final_sorted_output:
	print borough.title(), 
	print 'with',
	print number, 
	print 'complaints'
