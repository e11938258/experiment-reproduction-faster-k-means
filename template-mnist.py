from originalrepo.Code.kmeans import *
import sys



DATASET_BASE_LOCATION = "originalrepo/Dataset/" 
DATASET_NAME = "mnist768"
DIMENSIONALITY = 784

OBSERVATION_PRINT_THRESHOLD = 1000

def guardDimensionality(point):
	if len(point) != DIMENSIONALITY:
		raise Exception("Unexpected point length!")
		print(point)
		print(len(point))

def readMnistDataset():
	pointList = []
	observationsLoaded = 0
	# open file and read the content in a list
	with open(DATASET_BASE_LOCATION + DATASET_NAME, 'r') as filehandle:
	    for line in filehandle:
	        # remove linebreak which is the last character of the string
	        currentPointString = line[:-1]
	        # parse the points
	        currentPoint = currentPointString.split(",")
	        # convert to numbers
	        point = [float(point) for point in currentPoint if point != '']
	        # ensure point of correct size was extracted
	        guardDimensionality(point)
	        # add item to the list
	        pointList.append(point)
	        observationsLoaded += 1
	        if not len(pointList)%OBSERVATION_PRINT_THRESHOLD: print("Loaded", observationsLoaded, "observations")
	print("Dataset loaded with", len(pointList), "observations")
	return pointList

pointList = readMnistDataset()
k = 50
kmeansThreshold = 0.31
# k = Number of Clusters
# pointList = List of n-dimensional points (Every point should be a list)
# kmeansThreshold = Percentage Change in Mean Squared Error (MSE) below which the algorithm should stop. Used as a stopping criteria
# initialCentroids (optional) = Provide initial seeds for centroids (List of Point() class objects). It can be generated from a list of n-dimensional points as follows:
# initialCentroids = [Point(x,len(x)) for x in pointList]
Kmeans(k, pointList, kmeansThreshold, initialCentroids=None)