import csv
import shapefile
import sys
import numpy
from bokeh.plotting import *
def getZipBorough(zipBoroughFilename):
	with open(zipBoroughFilename) as f:
		csvReader=csv.reader(f)
		csvReader.next()
		return {row[0]:row[1] for row in csvReader}

def loadComplaints(filename,n):
	with open(filename) as f:
		csvread=csv.reader(f)
		header=next(csvread)
		Latitude=header.index('Latitude')
		Longitude=header.index('Longitude')
		lat=[]
		lng=[]
		for row in csvread:
			try:
				lat.append(float(row[Latitude]))
				lng.append(float(row[Longitude]))
			except:
				pass
	n=int(n)
	minx=min(lng)
	maxx=max(lng)
	miny=min(lat)
	maxy=max(lat)
	twodim={}
	for d in xrange(n):
		twodim[d]={}
		for e in xrange(n):
			twodim[d][e]=0
	for x,y in zip(lng,lat):
		if x<maxx:
			d=int(((x-minx)/(maxx-minx))*n)
		else:
			d=n-1
		if y<maxy:
			e=int(((y-miny)/(maxy-miny))*n)
		else:
			e=n-1
		twodim[d][e]+=1
	counts=[]
	cenlng=[]
	cenlat=[]
	for d in xrange(n):
		c_lng=(maxx-minx)*(float(d)/n)+(maxx-minx)/(2*n)+minx
		for e in xrange(n):
			counts.append(twodim[d][e])
			c_lat=(maxy-miny)*(float(e)/n)+(maxy-miny)/(2*n)+miny
			cenlng.append(c_lng)
			cenlat.append(c_lat)
	return counts,cenlat,cenlng
def matrix(counts,cenlat,cenlng,n):
	n=float(n)
	scatter(cenlng,cenlat,color='#99FF00',fill_alpha=0.5,line_alpha=0.3,size=[(c*n)/2000 for c in counts])
	hold(value=False)
	show()
def basemap(shapeFilename,zipBorough):
	shpdata=shapefile.Reader(shapeFilename)
	shpdict_all={'zip_x':[],'zip_y':[]}
	for r in shpdata.shapeRecords():
		if r.record[0] in zipBorough:
			parts=list(r.shape.parts) + [-1]
			points=[r.shape.points[parts[i]:parts[i+1]]\
				for i in xrange(len(r.shape.parts))]
			lngs = [p[0] for p in points[0]]
			lats = [p[1] for p in points[0]]
			shpdict_all['zip_y'].append(lngs)
			shpdict_all['zip_x'].append(lats)
	output_file("problem3.html",title="problem3")
	source=ColumnDataSource(data=shpdict_all)
	TOOLS="pan,wheel_zoom,box_zoom,reset,previewsave"
	patches('zip_y','zip_x',source=source,fill_color='#B8B8B8',\
		line_color="white",line_width=0.001 , tools=TOOLS,\
		plot_width=1100,plot_height=700,\
		title="311 complaints subdivisions")
	hold(value=True)

if __name__ == '__main__':
	if len(sys.argv) != 5:
		print 'Usage:'
		print sys.argv[0] \
		+ ' n <complaintsfilename> <zipboroughfilename> <shapefilename>'
		print '\ne.g.: ' + sys.argv[0] \
		+ ' 20 data/complaints.csv zip_borough.csv data/nyshape.shp'
	else:
		counts,cenlat,cenlng=loadComplaints(sys.argv[2],sys.argv[1])
		zipBorough=getZipBorough(sys.argv[3])
		basemap(sys.argv[4],zipBorough)
		matrix(counts,cenlat,cenlng,sys.argv[1])