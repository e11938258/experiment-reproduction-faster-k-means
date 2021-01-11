from originalrepo.Code.kmeans import *
import pandas as pd
import numpy as np

DATASET_BASE_LOCATION = "originalrepo/Dataset/" 


def loadcovtype():

         data = []
        with open(DATASET_BASE_LOCATION + 'covtype.data',"r", low_memory=False) as inputFile:
		for line in inputFile:
			data.append([float(x) for x in line.strip().split(delimiter)])
	return data







pointList = loadcovtype()
k = 50
kmeansThreshold = 0.31


# k = Number of Clusters
# pointList = List of n-dimensional points (Every point should be a list)
# kmeansThreshold = Percentage Change in Mean Squared Error (MSE) below which the algorithm should stop. Used as a stopping criteria
# initialCentroids (optional) = Provide initial seeds for centroids (List of Point() class objects). It can be generated from a list of n-dimensional points as follows:
# initialCentroids = [Point(x,len(x)) for x in pointList]
Kmeans(k, pointList, kmeansThreshold, initialCentroids=None)