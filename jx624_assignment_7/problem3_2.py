import csv,sys
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


#####get the zip code dict
z311={}
with open (sys.argv[2]) as f1:
	csvread=csv.reader(f1)
	header=next(csvread)
	for row in csvread:
		try:
			code=int(row[0].strip()[:5])
			z311[code]=int(row[1])
		except:
			pass



#####get the 311 data dict
zipcode={}
hand=[]
agencycolor={'NYPD':'r','DOT':'b','DOB':'g','TLC':'y','DPR':'pink','other':'grey'}
# color_a = dict((v,k) for k,v in agencycolor.iteritems())
for k,v in agencycolor.iteritems():
	red_patch = mpatches.Patch(color=v, label=k)
	hand.append(red_patch)
with open (sys.argv[1]) as f1:
	csvread=csv.reader(f1)
	header=next(csvread)
	for row in csvread:
		agency=row[3].strip()
		##define color
		if agency in agencycolor:
			agency=agencycolor[agency]
		else:
			agency=agencycolor['other']
		##import data: zipcode--agency(color)--count
		try:
			code=int(row[8].strip()[:5])
			if code in zipcode:
				if agency in zipcode[code]:
					zipcode[code][agency]+=1
				else:
					zipcode[code][agency]=1
			else:
				zipcode[code]={}
				if agency in zipcode[code]:
					zipcode[code][agency]+=1
				else:
					zipcode[code][agency]=1
		except:
			pass
zipcode.pop(0, None)



##get the total volume, population and the color ----->plot scatter plot!
for code in zipcode:
	

	##total volume
	count=0
	for agency in zipcode[code]:
		count +=int(zipcode[code][agency])
	

	##color
	try:
		zipcode[code].pop('grey', None)
		colorofdot=max(zipcode[code].iteritems(), key=lambda x:x[1])[0]
		a=0.5
	except:
		colorofdot='grey'
		a=0.3
	##population
	try:
		if code in z311:
			population=z311[code]
			plt.scatter(population,count,color=colorofdot,alpha=a)
	except:
		pass
plt.ylabel('Volume')
plt.xlabel('population')
plt.title('The scatter of different zipcode') 
plt.legend(handles= hand,loc=2)
plt.show()
# zipcode_311=df(z311.values(),index=z311.keys())
# data=pandas.merge(zipcode_s,zipcode_311,how='inner',left_index=True, right_index=True)
# plt.scatter(data['0_y'],data['0_x'],alpha=0.3)
# plt.show()


