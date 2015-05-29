import sys
import time
import csv
from scipy.spatial import KDTree
from collections import Counter
import matplotlib.pyplot as plt
def loadTaxiTripsPickupAndDropoffs(filename):
    #bbox around Manhattan
    latBounds = [40.6,40.9]
    lngBounds = [-74.05,-73.90]
    #
    f = open(filename)
    reader = csv.reader(f)
    header = reader.next()
    #
    lngIndex0 = header.index(' pickup_longitude')
    latIndex0 = header.index(' pickup_latitude')
    latIndex1 = header.index(' dropoff_latitude')
    lngIndex1 = header.index(' dropoff_longitude')
    result = []
    for l in reader:
        try:
            point0 = [float(l[latIndex0]),float(l[lngIndex0])]
            point1 = [float(l[latIndex1]),float(l[lngIndex1])]
            if latBounds[0] <= point0[0] <= latBounds[1] and lngBounds[0] <= point0[1] <= lngBounds[1] and latBounds[0] <= point1[0] <= latBounds[1] and lngBounds[0] <= point1[1] <= lngBounds[1]:
                result.append([point0[0],point0[1],point1[0],point1[1]])
        except:
            print l
    return result
    
def naiveApproach(tripLocations, startRectangle, endRectangle):
    #indices is a list that should contain the indices of the trips in the tripLocations list
    #which start in the startRectangle region and end in the endRectangle region

    #TODO: insert your code here. You should implement the naive approach, i.e., loop 
    #      through all the trips and find the closest intersection by looping through
    #      all of them
    indices = []
    startTime = time.time()
    n = 0
    for point in tripLocations:
        if startRectangle[0][1]>=point[0]>=startRectangle[0][0]and startRectangle[1][1]>=point[1]>=startRectangle[1][0] and startRectangle[0][1]>=point[2]>=startRectangle[0][0]and startRectangle[1][1]>=point[3]>=startRectangle[1][0]:
            indices.append(n)
        n+=1

    #
    endTime = time.time()
    print 'The naive computation took', (endTime - startTime), 'seconds'
    return indices

def kdtreeApproach(tripLocations, startRectangle, endRectangle):
    #indices is a list that should contain the indices of the trips in the tripLocations list
    #which start in the startRectangle region and end in the endRectangle region
    indices = []
    startTime = time.time()

    #TODO: insert your code here. You should build the kdtree and use it to query the closest
    #      intersection for each trip
    startpoint = []
    endpoint = []
    for item in tripLocations:
        startpoint.append([item[0],item[1]])
        endpoint.append([item[2],item[3]])
    #print start
    startTime = time.time()



    rs = ((startRectangle[0][0] - startRectangle[0][1])**2 + (startRectangle[1][0] - startRectangle[1][1])**2)**0.5/float(2)
    re = ((endRectangle[0][0] - endRectangle[0][1])**2 + (endRectangle[1][0] - endRectangle[1][1])**2)**0.5/float(2)
    os = [(startRectangle[0][0] + startRectangle[0][1])/2,(startRectangle[1][0] + startRectangle[1][1])/2]
    oe = [(endRectangle[0][0] + endRectangle[0][1])/2,(endRectangle[1][0] + endRectangle[1][1])/2]


    Stree = KDTree(startpoint)
    Etree = KDTree(endpoint)
    startpoint = set(Stree.query_ball_point(os, rs))
    endpoint = set(Etree.query_ball_point(oe, re))
    s_e = list(startpoint.intersection(endpoint))
    for point in s_e:
        if startRectangle[0][1]>=tripLocations[point][0]>=startRectangle[0][0]and startRectangle[1][1]>=tripLocations[point][1]>=startRectangle[1][0] and startRectangle[0][1]>=tripLocations[point][2]>=startRectangle[0][0]and startRectangle[1][1]>=tripLocations[point][3]>=startRectangle[1][0]:
            indices.append(i)
    #
    endTime = time.time()
    print 'The kdtree computation took', (endTime - startTime), 'seconds'
    return indices

def point_inside_polygon(x,y,poly):

    n = len(poly)
    inside =False

    p1x,p1y = poly[0]
    for i in range(n+1):
        p2x,p2y = poly[i % n]
        if y > min(p1y,p2y):
            if y <= max(p1y,p2y):
                if x <= max(p1x,p2x):
                    if p1y != p2y:
                        xinters = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x,p1y = p2x,p2y

    return inside

def extraCredit(tripLocations, startPolygon, endPolygon):
    #indices is a list that should contain the indices of the trips in the tripLocations list
    #which start in the startPolygon region and end in the endPolygon region
    indices = []

    #TODO: insert your code here. You should build the kdtree and use it to query the closest
    #      intersection for each trip
    startpoint = []
    endpoint = []
    for item in tripLocations:
        startpoint.append([item[0],item[1]])
        endpoint.append([item[2],item[3]])
    #print start
    startTime = time.time()



    rs = ((startRectangle[0][0] - startRectangle[0][1])**2 + (startRectangle[1][0] - startRectangle[1][1])**2)**0.5/float(2)
    re = ((endRectangle[0][0] - endRectangle[0][1])**2 + (endRectangle[1][0] - endRectangle[1][1])**2)**0.5/float(2)
    os = [(startRectangle[0][0] + startRectangle[0][1])/2,(startRectangle[1][0] + startRectangle[1][1])/2]
    oe = [(endRectangle[0][0] + endRectangle[0][1])/2,(endRectangle[1][0] + endRectangle[1][1])/2]


    Stree = KDTree(startpoint)
    Etree = KDTree(endpoint)
    startpoint = set(Stree.query_ball_point(os, rs))
    endpoint = set(Etree.query_ball_point(oe, re))
    s_e = list(startpoint.intersection(endpoint))
    for point in s_e:
        if point_inside_polygon(tripLocations[point][0],tripLocations[point][1],startPolygon) and point_inside_polygon(tripLocations[point][2],tripLocations[point][3],endPolygon):
            indices.append(i)
    return indices    

if __name__ == '__main__':
    #these functions are provided and they already load the data for you
    trips             = loadTaxiTripsPickupAndDropoffs(sys.argv[1])
    #
    startRectangle    = [[40.713590,40.721319],[-74.011116,-73.994722]] #[[minLat,maxLat],[minLng,maxLng]]
    endRectangle      = [[40.744532,40.748398],[-74.003005,-73.990881]] #[[minLat,maxLat],[minLng,maxLng]]

    #You need to implement this one. You need to make sure that the counts are correct
    naiveIndices = naiveApproach(trips,startRectangle, endRectangle)

    #You need to implement this one. You need to make sure that the counts are correct
    kdtreeIndices = kdtreeApproach(trips,startRectangle, endRectangle)
