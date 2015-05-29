import csv,shapefile,sys
from bokeh.plotting import *
from bokeh.objects import HoverTool,ColumnDataSource
from collections import OrderedDict
colors={'NYPD':'#E82A37',
			'DOT' :'#F35E4C',
			'DEP' :'#A64847',
			'FDNY':'#0DA921',
			'HPD' :'#F6A615',
			'DOHMH':'#ADFF85',
			'TLC':'#3C74F7',
			'DPR':'#70B8FF'} 
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
		agencyIndex=header.index('Agency')
		complaintdictbyzip={}
		for row in csvread:
			try:
				agency=row[agencyIndex]
				zipcode=row[zipIndex][:5]
				if zipcode in complaintdictbyzip:
					if agency in complaintdictbyzip[zipcode]:
						complaintdictbyzip[zipcode][agency]+=1
					else:
						complaintdictbyzip[zipcode][agency]=1
				else:
					complaintdictbyzip[zipcode]={}
					complaintdictbyzip[zipcode][agency]=1
			except:
				pass
		
		return complaintdictbyzip

def readshp(shapeFilename,complaintdictbyzip,zipBorough):
	shpdata=shapefile.Reader(shapeFilename)
	shpdict_all={'zip_x':[],'zip_y':[],'zip_color':[],'zip_agency':[],'zip_code':[],'zip_maxcount':[]}
	for r in shpdata.shapeRecords():
		if r.record[0] in zipBorough:
			parts=list(r.shape.parts) + [-1]
			points=[r.shape.points[parts[i]:parts[i+1]] for i in xrange(len(r.shape.parts))]
			lngs = [p[0] for p in points[0]]
			lats = [p[1] for p in points[0]]
			
			if r.record[0] in complaintdictbyzip:
				tuplec=max(complaintdictbyzip[r.record[0]].items(),key=lambda x: x[1])
				agency=tuplec[0]
				count=tuplec[1]
				color=colors[agency]
			else:
				color='gray'
				agency='unknown'
				count='unknown'

			shpdict_all['zip_color'].append(color)
			shpdict_all['zip_agency'].append(agency)
			shpdict_all['zip_maxcount'].append(count)
			shpdict_all['zip_y'].append(lngs)
			shpdict_all['zip_x'].append(lats)
			shpdict_all['zip_code'].append(r.record[0])
	return shpdict_all
def drawPlot(shpdict_all):	
	output_file("problem1.html",title="problem1")
	source=ColumnDataSource(data=shpdict_all)
	TOOLS="pan,wheel_zoom,box_zoom,reset,hover,previewsave"
	patches('zip_y','zip_x',source=source,fill_color='zip_color',\
		line_color='#708090',line_width=0.001 , tools=TOOLS,plot_width=1100,plot_height=700, \
		title="Top agencies by zip code")	
	hover=curplot().select(dict(type=HoverTool))
	hover.tooltips=OrderedDict([
		('Zip Code','@zip_code'),
		('Top Agency','@zip_agency'),
		('Complaints','@zip_maxcount')])
	hold()
	x,y=-74.2,40.85
	for a,b in colors.iteritems():
		rect([x],[y],color=b,width=0.025,height=0.008)
		text([x-0.02],[y],text=a,angle=0,text_font_size="10pt",text_align="right",text_baseline="middle")
		y=y+0.012
	
	show()

if __name__ == '__main__':
	if len(sys.argv) != 4:
		print 'error'
	else:
		complaintdictbyzip=loadComplaints(sys.argv[1])
		zipBor=getZipB(sys.argv[2])
		shpdict_all=readshp(sys.argv[3], complaintdictbyzip, zipBor)
		drawPlot(shpdict_all)
