# import sys
# import random
# import time
# import math

# #Test if plot modules are available
# import imp
# try:
# 	import matplotlib.pyplot as plt
# 	import numpy as np
# 	foundPlotModules = True
# except ImportError:
# 	foundPlotModules = False

# def generateSampleInput(inputSize):
# 	sampleInput = []
# 	for i in xrange(inputSize):
# 		sampleInput.append((random.random(), random.random()))
# 	return sampleInput

# Functions for students to implement.
naive = []
def buildNaive(points,n):
	naive[:] = []
	for item in points:
		naive.append(item)
	#your code here

	

onedim = []
num=0
def buildOneDim(points,n):
	onedim[:]=[]
	global num
	num=n
	for i in xrange(num):
		onedim.append([])
	for item in points:
		if int(item[0])<1:
			columnum=int(item[0]*num)
		else:
			columnum=num-1
		onedim[columnum].append(item)
	#your code here


twodim = []
def buildTwoDim(points,n):
	twodim[:] =[]#erasing previous data
	global num
	num=n
	for i in xrange(num):
		twodim.append([])
		for j in xrange(num):
			twodim[i].append([])
	for item in points:
		if int(item[0])<1:
			columnumx=int(item[0]*num)
		else:
			columnumx=num-1
		if int(item[1])<1:
			columnumy=int(item[1]*num)
		else:
			columnumy=num-1
		twodim[columnumx][columnumy].append(item)
	#your code here
	return None


def queryNaive(x0, y0, x1, y1):
	count = 0
	for item in naive:
		if item[0]>=x0 and item[0]<=x1 and item[1]>=y0 and item[1]<=y1:
			count+=1
	return count
	#your code here

def querydim(x0):
	if x0<1:
		querydimx0=int(x0*num)
	else:
		querydimx0=num-1
	return querydimx0

def queryOneDim(x0, y0, x1, y1):
	count = 0
	dimx0=querydim(x0)
	dimx1=querydim(x1)
	if (dimx1-dimx0)==0:
		for item in onedim[dimx0]:
			if item[0]>=x0 and item[0]<=x1 and item[1]>=y0 and item[1]<=y1:
				count+=1
	if (dimx1-dimx0)>1:
		for dimnum in xrange(dimx0+1,dimx1):
			for item in onedim[dimnum]:
				if item[1]>=y0 and item[1]<=y1:
					count+=1
		for item in onedim[dimx0]:
			if item[1]>=y0 and item[1]<=y1 and item[0]>=x0:
				count+=1
		for item in onedim[dimx1]:
			if item[1]>=y0 and item[1]<=y1 and item[0]<=x1:
				count+=1
	if(dimx1-dimx0)==1:
		for item in onedim[dimx0]:
			if item[1]>=y0 and item[1]<=y1 and item[0]>=x0:
				count+=1
		for item in onedim[dimx1]:
			if item[1]>=y0 and item[1]<=y1 and item[0]<=x1:
				count+=1
	return count

def queryTwoDim(x0, y0, x1, y1):
	count = 0
	dimx0=querydim(x0)
	dimx1=querydim(x1)
	dimy0=querydim(y0)
	dimy1=querydim(y1)
	for dimx in twodim[dimx0:dimx1+1]:
		for dimy in dimx[dimy0:dimy1+1]:
			for item in dimy:
				if item[0]>=x0 and item[0]<=x1:
					if item[1]>=y0 and item[1]<=y1:
						count+=1
	return count
# if __name__ == '__main__':
# 	sampleInput = generateSampleInput(1000000)
# 	buildOneDim(sampleInput,1)
# 	x0 = random.uniform(0,1)
# 	y0 = random.uniform(0,1)
# 	x1 = random.uniform(x0,1)
# 	y1 = random.uniform(y0,1)
# 	startTime = time.time()
# 	b=queryOneDim(x0,y0,x1,y1)
# 	ellapsedTime  = time.time() - startTime
# 	print b

