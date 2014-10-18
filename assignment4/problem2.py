def searchGreaterNotSorted(L, v):
	count=0
	for item in L:
		if item >v:
			count+=1
	return count

def searchGreaterSorted(L, v):
	lens=len(L)
	for item in L:
		if item>v:
			lens=L.index(item)
			break

	return len(L)-lens

def searchGreaterBinSearch(L, v):
	hi = len(L)-1
	lo=0
	while lo < hi:
		mid = (lo+hi)//2
		if v < L[mid]: 
			hi = mid-1
		else: lo = mid+1
	if L[lo]<=v:
		n=len(L)-lo-1
	else:
		n=len(L)-lo
	return n

def searchInRange(L, v1, v2):
	left=searchGreaterBinSearch(L,v1)
	right=searchGreaterBinSearch(L,v2)
	num=left-right
	if num<0 : num=0
	return num


