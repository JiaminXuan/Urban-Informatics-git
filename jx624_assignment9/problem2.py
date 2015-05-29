import csv,shapefile,sys
from bokeh.plotting import *
from bokeh.objects import HoverTool,ColumnDataSource
from collections import OrderedDict
colorscale=['#000033','#000066','#000099','#0000CC','#0000FF','#0000FF','#3333FF','#6666FF','#9999FF','#CCCCFF']

def getZipBorough(zipBoroughFilename):
	with open(zipBoroughFilename) as f:
		csvReader=csv.reader(f)
		csvReader.next()
		return {row[0]:row[1] for row in csvReader}

def loadComplaints(filename,agency1,agency2):
	agencylist=[agency1,agency2]
	with open(filename) as f:
		csvread=csv.reader(f)
		header=next(csvread)
		zipIndex=header.index('Incident Zip')
		agencyIndex=header.index('Agency')
		complaintdictbyzip={}
		for row in csvread:
			try:
				agency=row[agencyIndex]
				zipCode=row[zipIndex][:5]
				if agency in agencylist: 
					if zipCode in complaintdictbyzip:
						if agency in complaintdictbyzip[zipCode]:
							complaintdictbyzip[zipCode][agency]+=1
						else:
							complaintdictbyzip[zipCode][agency]=1
					else:
						complaintdictbyzip[zipCode]={}
						complaintdictbyzip[zipCode][agency]=1
			except:
				pass
	return complaintdictbyzip



def readshp(shapeFilename,complaintdictbyzip,zipBorough,agency1,agency2):
	shpdata=shapefile.Reader(shapeFilename)
	shpdict_all={'zip_x':[],'zip_y':[],'zip_color':[]}
	for r in shpdata.shapeRecords():
		if r.record[0] in zipBorough:
			parts=list(r.shape.parts) + [-1]
			points=[r.shape.points[parts[i]:parts[i+1]] for i in xrange(len(r.shape.parts))]
			lngs = [p[0] for p in points[0]]
			lats = [p[1] for p in points[0]]

			if r.record[0] in complaintdictbyzip:
				try:
					count1=complaintdictbyzip[r.record[0]][agency1]
				except:
					count1=0
				try:
					count2=complaintdictbyzip[r.record[0]][agency2]
				except:
					count2=0
				colorIndex=(float(count1)/(count1+count2))*len(colorscale)
				color=colorscale[int(colorIndex)-1]
			else:
				color='gray'

			shpdict_all['zip_color'].append(color)
			shpdict_all['zip_y'].append(lngs)
			shpdict_all['zip_x'].append(lats)
	return shpdict_all
def drawPlot(shpdict_all,agency1,agency2):
	output_file("problem2.html",title="problem2")
	source=ColumnDataSource(data=shpdict_all)
	TOOLS="pan,wheel_zoom,box_zoom,reset,previewsave"
	patches('zip_y','zip_x',source=source,fill_color='zip_color',\
		line_color="gray",line_width=0.0000001 , tools=TOOLS,\
		plot_width=1100,plot_height=700,\
		title="%s v.s. %s by zip code" %(agency1,agency2))
	hold()
	x,y=-74.2,40.85
	text([x-0.015],[y],text='100% '+agency2,angle=0,text_font_size="9pt",text_align="right",text_baseline="middle")
	for c in colorscale:
		rect([x],[y],color=c,width=0.025,height=0.01)
		y=y+0.01
	text([x-0.015],[y-0.005],text='100% '+agency1,angle=0,text_font_size="9pt",text_align="right",text_baseline="top")
		
	show()

if __name__ == '__main__':
	if len(sys.argv) != 6:
		print 'Usage:'
		print sys.argv[0] \
		+ ' <complaintsfilename> <zipboroughfilename> <shapefilename> <agency1> <agency2> '
		print '\ne.g.: ' + sys.argv[0] \
		+ ' data/complaints.csv zip_borough.csv data/nyshape.shp NYPD FDNY'
	else:
		data=loadComplaints(sys.argv[1],sys.argv[4],sys.argv[5])
		zipBorough=getZipBorough(sys.argv[2])
		shpdict_all=readshp(sys.argv[3],data,zipBorough,sys.argv[4],sys.argv[5])
		drawPlot(shpdict_all,sys.argv[4],sys.argv[5])