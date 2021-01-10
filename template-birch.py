import originalrepo.Code.kmeans as def_kmeans 
import originalrepo.Code.heuristic_kmeans as heur_kmeans
import time
import os

# input dataset configuration
DATASET_BASE_LOCATION = "originalrepo/Dataset/" 
DATASET_NAME = 'birch.txt'

# repetition configuration
REPETITION_COUNT = 10

# output destination configuration
RESULTS_FOLDER = "results/"
RESULTS_RUNNER_NAME = "NONE"
RESULT_BASE_FILENAME= "birch"

def readBirchDataset():
	pointList = []
	# open file and read the content in a list
	with open(DATASET_BASE_LOCATION + DATASET_NAME, 'r') as filehandle:
	    for line in filehandle:
	        # remove linebreak which is the last character of the string
	        currentPointString = line[:-1]
	        # parse the points
	        currentPoint = currentPointString.split("    ")
	        # convert to numbers
	        point = [int(point) for point in currentPoint if point != '']
	        # add item to the list
	        pointList.append(point)
	
	return pointList

def outputRuntimes(runtimeDefault, runtimeHeuristic):
	# create the results folder if doesn't exist
	if not os.path.exists(RESULTS_FOLDER):
		os.makedirs(RESULTS_FOLDER)
	# write the runtimes
	timestamp = str(int(time.time()))
	with open(RESULTS_FOLDER + RESULT_BASE_FILENAME + "-" + RESULTS_RUNNER_NAME + "-" +timestamp, 'w') as filehandle:
		filehandle.write(",".join([str(runtime) for runtime in runtimeDefault]))
		filehandle.write("\n")
		filehandle.write(",".join([str(runtime) for runtime in runtimeHeuristic]))


repetitionsRun = 0
timeTakenDefault = []

# initialize the parameters
pointList = readBirchDataset()
k = 50
kmeansThreshold = 0.31


while repetitionsRun < REPETITION_COUNT:
	start_time = time.time()
	# k = Number of Clusters
	# pointList = List of n-dimensional points (Every point should be a list)
	# kmeansThreshold = Percentage Change in Mean Squared Error (MSE) below which the algorithm should stop. Used as a stopping criteria
	# initialCentroids (optional) = Provide initial seeds for centroids (List of Point() class objects). It can be generated from a list of n-dimensional points as follows:
	# initialCentroids = [Point(x,len(x)) for x in pointList]
	def_kmeans.Kmeans(k, pointList, kmeansThreshold, initialCentroids=None)
	timeTakenDefault.append(time.time() - start_time)
	repetitionsRun += 1

print "Done running the NON-HEURISTIC approach"

# set additional heuristic specific parameters
centroidsToRemember = k * 0.4
# reset the repetition counter
repetitionsRun = 0
timeTakenHeur = []
while repetitionsRun < REPETITION_COUNT:
	start_time = time.time()
	# k = Number of Clusters
	# pointList = List of n-dimensional points (Every point should be a list)
	# kmeansThreshold = Percentage Change in Mean Squared Error (MSE) below which the algorithm should stop. Used as a stopping criteria
	# initialCentroids (optional) = Provide initial seeds for centroids (List of Point() class objects). It can be generated from a list of n-dimensional points as follows:
	# initialCentroids = [Point(x,len(x)) for x in pointList]
	heur_kmeans.Kmeans(k, pointList, kmeansThreshold, centroidsToRemember, initialCentroids=None)
	timeTakenHeur.append(time.time() - start_time)
	repetitionsRun += 1

print "Done running the HEURISTIC approach"

outputRuntimes(timeTakenDefault, timeTakenHeur)