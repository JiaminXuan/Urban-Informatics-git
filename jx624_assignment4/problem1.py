# Functions for students to implement.
def solveOnlyLists(inputList):
	uniqueList = []
	for item in inputList:
		if item not in uniqueList:
			uniqueList.append(item)
	return uniqueList

# def solveListswithHash(inputList):
# 	uniqueList = []
# 	for item in inputList:
# 		if item not in uniqueList:
# 			uniqueList.append(item)
# 	return uniqueList
def solveDict(inputList):
	uniqueList = []
	uniquedict={}
	for item in inputList:
		if item not in uniquedict:
			uniquedict[item]=item
	uniqueList=list(uniquedict.keys())
	return uniqueList

def solveSorted(sortedInputList):
	uniqueList = []
	lastdigit=sortedInputList[0]
	for item in sortedInputList:
		if item!=lastdigit:
			uniqueList.append(item)
			lastdigit=item

	#compute unique items in inputList
	return uniqueList

