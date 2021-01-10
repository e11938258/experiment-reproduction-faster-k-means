from originalrepo.Code.kmeans import *
import sys
import numpy as np
import cPickle as pickle


DATASET_BASE_LOCATION = "originalrepo/Dataset/" 
DATASET_NAME = "synthetic"

def readSyntheticDataset():
	with open(DATASET_BASE_LOCATION + DATASET_NAME, "rb") as f:
		numpyPointList = pickle.load(f)
	return numpyPointList.tolist()

pointList = readSyntheticDataset()
k = 50
kmeansThreshold = 0.31



# k = Number of Clusters
# pointList = List of n-dimensional points (Every point should be a list)
# kmeansThreshold = Percentage Change in Mean Squared Error (MSE) below which the algorithm should stop. Used as a stopping criteria
# initialCentroids (optional) = Provide initial seeds for centroids (List of Point() class objects). It can be generated from a list of n-dimensional points as follows:
# initialCentroids = [Point(x,len(x)) for x in pointList]
Kmeans(k, pointList, kmeansThreshold, initialCentroids=None)