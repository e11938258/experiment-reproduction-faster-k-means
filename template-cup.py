from originalrepo.Code.kmeans import *
import pandas as pd
import numpy as np

DATASET_BASE_LOCATION = "originalrepo/Dataset/"


def loadCupDataset():
	data = []
	data = pd.read_csv('originalrepo/Dataset/'cup98LRN.txt', low_memory=False)
	data = data.fillna(0)

	cat_columns = data.select_dtypes([np.object]).columns
	for col in cat_columns:
		data[col] = data[col].astype('category')

	cat_columns = data.select_dtypes(['category']).columns
	data[cat_columns] = data[cat_columns].apply(lambda x: x.cat.codes)

	return data.values.tolist()


pointList = loadCupDataset()
k = 50
kmeansThreshold = 0.31

# k = Number of Clusters
# pointList = List of n-dimensional points (Every point should be a list)
# kmeansThreshold = Percentage Change in Mean Squared Error (MSE) below which the algorithm should stop. Used as a stopping criteria
# initialCentroids (optional) = Provide initial seeds for centroids (List of Point() class objects). It can be generated from a list of n-dimensional points as follows:
# initialCentroids = [Point(x,len(x)) for x in pointList]
Kmeans(k, pointList, kmeansThreshold, initialCentroids=None)