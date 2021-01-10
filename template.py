from originalrepo.Code.kmeans import *



DATASET_BASE_LOCATION = "originalrepo/Dataset/" 

# define an empty list

def readBirchDataset():
	pointList = []
	# open file and read the content in a list
	with open(DATASET_BASE_LOCATION + 'birch.txt', 'r') as filehandle:
	    for line in filehandle:
	        # remove linebreak which is the last character of the string
	        currentPointString = line[:-1]
	        # parse the points
	        currentPoint = currentPointString.split("    ")
	        # drop the first element (empty space)
	        # convert to numbers
	        point = [int(point) for point in currentPoint if point != '']
	        # add item to the list
	        pointList.append(point)
	
	return pointList

pointList = readBirchDataset()
k = 50
kmeansThreshold = 0.31

# k = Number of Clusters
# pointList = List of n-dimensional points (Every point should be a list)
# kmeansThreshold = Percentage Change in Mean Squared Error (MSE) below which the algorithm should stop. Used as a stopping criteria
# initialCentroids (optional) = Provide initial seeds for centroids (List of Point() class objects). It can be generated from a list of n-dimensional points as follows:
# initialCentroids = [Point(x,len(x)) for x in pointList]
Kmeans(k, pointList, kmeansThreshold, initialCentroids=None)