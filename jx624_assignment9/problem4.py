import csv
import shapefile
import sys
from bokeh.plotting import *
import numpy

def getZipB(zipBf):
	with open(zipBf) as f:
		csvReader=csv.reader(f)
		csvReader.next()
		return {row[0][:5]:row[1] for row in csvReader}

def loadComplaints(filename):
	with open(filename) as f:
		csvread=csv.reader(f)
		header=next(csvread)
		zipIndex=header.index('Incident Zip')
		complaintdictbyzip={}
		for row in csvread:
			try:
				zipcode=row[zipIndex][:5]
				if zipcode in complaintdictbyzip:
					complaintdictbyzip[zipcode]+=1
				else:
					complaintdictbyzip[zipcode]=1
			except:
				pass
		
		return complaintdictbyzip

def getZipBorough(zipBoroughFilename):
	with open(zipBoroughFilename) as f:
		csvReader=csv.reader(f)
		csvReader.next()

		return {row[0]:row[1] for row in csvReader}

def maps(shapeFilename,zipBorough):
	shpdata=shapefile.Reader(shapeFilename)
	shpdict_all={'zip_x':[],'zip_y':[]}
	dots={}
	for r in shpdata.shapeRecords():
		if r.record[0] in zipBorough:
			dots[r.record[0]]=[]
			parts=list(r.shape.parts) + [-1]
			points=[r.shape.points[parts[i]:parts[i+1]]\
				for i in xrange(len(r.shape.parts))]
			lngs = [p[0] for p in points[0]]
			lats = [p[1] for p in points[0]]
			shpdict_all['zip_y'].append(lngs)
			dots[r.record[0]].append(numpy.mean(lngs))
			shpdict_all['zip_x'].append(lats)
			dots[r.record[0]].append(numpy.mean(lats))
	output_file("problem4.html",title="problem4")
	TOOLS="pan,wheel_zoom,box_zoom,reset,previewsave"
	patches(shpdict_all['zip_y'],shpdict_all['zip_x'],fill_color='#B8B8B8',\
		line_color="white",line_width=0.001 , tools=TOOLS,\
		plot_width=1100,plot_height=700,\
		title="311 complaints subdivisions")
	hold(value=True)
	return dots
def points(dots,complaintdictbyzip):
	lngdd=[]
	latdd=[]
	counts=[]
	for zipcodes in dots:
		try:
			counts.append(complaintdictbyzip[zipcodes])
			lngdd.append(dots[zipcodes][0])
			latdd.append(dots[zipcodes][1])
		except:
			pass
	scatter(lngdd,latdd,color='#99FF00',fill_alpha=0.5,line_alpha=0.3,\
		size=[c/100 for c in counts])
	hold(value=False)
	show()
	
if __name__ == '__main__':
	# if len(sys.argv) != 4:
	#   print 'Usage:'
	#   print sys.argv[0] \
	#   + ' <complaintsfilename> <zipboroughfilename> <shapefilename>'
	#   print '\ne.g.: ' + sys.argv[0] \
	#   + ' data/complaints.csv zip_borough.csv data/nyshape.shp'
	# else:
		complaintdictbyzip=loadComplaints(sys.argv[1])
		zipBorough=getZipB(sys.argv[2])
		dots=maps(sys.argv[3],zipBorough)
		points(dots,complaintdictbyzip)