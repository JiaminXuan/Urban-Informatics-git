import sys
import time
import csv
from scipy.spatial import KDTree
from collections import Counter
import matplotlib.pyplot as plt
def loadRoadNetworkIntersections(filename):
	#bbox around Manhattan
	latBounds = [40.6,40.9]
	lngBounds = [-74.05,-73.90]
	#
	listWithIntersectionCoordinates = []
	f = open(filename)
	reader = csv.reader(f, delimiter=' ')
	for l in reader:
		try:
			point = [float(l[0]),float(l[1])]
			if latBounds[0] <= point[0] <= latBounds[1] and lngBounds[0] <= point[1] <= lngBounds[1]:
				listWithIntersectionCoordinates.append(point)
		except:
			print l

	return listWithIntersectionCoordinates

def loadTaxiTrips(filename):
	#load pickup positions
	loadPickup = True
	#bbox around Manhattan
	latBounds = [40.6,40.9]
	lngBounds = [-74.05,-73.90]
	#
	f = open(filename)
	reader = csv.reader(f)
	header = reader.next()
	#
	if loadPickup:        
		lngIndex = header.index(' pickup_longitude')
		latIndex = header.index(' pickup_latitude')
	else:
		latIndex = header.index(' dropoff_latitude')
		lngIndex = header.index(' dropoff_longitude')
	result = []
	for l in reader:
		try:
			point = [float(l[latIndex]),float(l[lngIndex])]
			if latBounds[0] <= point[0] <= latBounds[1] and lngBounds[0] <= point[1] <= lngBounds[1]:
				result.append(point)

		except:
			print l
	return result
	
def naiveApproach(intersections, tripLocations):
	 #counts is a dictionary that has as keys the intersection index in the intersections list
	#and as values the number of trips in the tripLocation list which has the key as the closest
	#intersection.
	counts = {}
	mindist = 99999999
	startTime = time.time()
	
		
	#TODO: insert your code here. You should implement the naive approach, i.e., loop 
	#      through all the trips and find the closest intersection by looping through
	#      all of them
	for i in tripLocations:
			for j in intersections:
				dist=(i[0]-j[0])**2+(i[1]-j[1])**2
				if dist<mindist:
					mindist = dist
					x=j[0]
					y=j[1]
			count = counts.setdefault((x,y), 0)
			counts[(x,y)]+=1

	#
	endTime = time.time()
	print 'The naive computation took', (endTime - startTime), 'seconds'
	return counts

def kdtreeApproach(intersections, tripLocations):
	#counts is a dictionary that has as keys the intersection index in the intersections list
	#and as values the number of trips in the tripLocation list which has the key as the closest
	#intersection.
	counts = {}
	startTime = time.time()

	#TODO: insert your code here. You should build the kdtree and use it to query the closest
	#      intersection for each trip
	tree = KDTree(intersections)
	distance,index = tree.query(tripLocations,k = 1)
	counts = Counter(index)


	#
	endTime = time.time()
	print 'The kdtree computation took', (endTime - startTime), 'seconds'
	return counts

def plotResults(intersections, counts):
	#TODO: intersect the code to plot here
	# high = max(counts.values())
	# low = min(counts.values())
	a = set(counts.keys())
	l = set(range(len(intersections)))
	b = list(l - a)
	for i in b:
		counts.setdefault(i, 4)
	for i in counts.keys():
		plt.plot(intersections[i][1], intersections[i][0], 'bo', ms = counts[i]/4) #alpha = counts[i]/float(high))
	#for i in b:

if __name__ == '__main__':
	#these functions are provided and they already load the data for you
	roadIntersections = loadRoadNetworkIntersections(sys.argv[1])
	tripPickups       = loadTaxiTrips(sys.argv[2])
	#You need to implement this one. You need to make sure that the counts are correct
	naiveCounts = naiveApproach(roadIntersections,tripPickups)

	#You need to implement this one. You need to make sure that the counts are correct
	kdtreeCounts = kdtreeApproach(roadIntersections,tripPickups)

	#
	plotResults(roadIntersections,kdtreeCounts)
	plt.show()