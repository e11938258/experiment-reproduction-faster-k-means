import originalrepo.Code.kmeans as def_kmeans 
import originalrepo.Code.heuristic_kmeans as heur_kmeans

import originalrepo.Code.triangleInequality as def_inequality 
import originalrepo.Code.heuristic_triangleinequality as heur_inequality

import originalrepo.Code.enhancedKmeans as def_enhanced 
import originalrepo.Code.heuristic_enhancedKmeans as heur_enhanced

import time
import os

# input dataset configuration
DATASET_BASE_LOCATION = "originalrepo/Dataset/" 
DATASET_NAME = 'birch.txt'

# repetition configuration
REPETITION_COUNT = 10
MSE_TO_CONVERGE = 5*pow(10,13)
MSE_TO_CONVERGE_SMALL = 4.75*pow(10,13)


# output destination configuration
RESULTS_FOLDER = "results/"
RESULTS_RUNNER_NAME = "NONE"
RESULT_BASE_FILENAME= "birch-"

# experiment parameter combinations
parameterCombinations = [
# (k, 	kmeansThreshold, 			centroidsToRemember, 	seedType, 	PIM,	algorithm)
  (100, MSE_TO_CONVERGE,	 		20, 					"random", 	0.01,	"kmeans"),
  (100, MSE_TO_CONVERGE,	 		30, 					"random", 	0,		"kmeans"),
  (100, MSE_TO_CONVERGE, 			40, 					"random", 	0,		"kmeans"),
  (100, MSE_TO_CONVERGE, 			50, 					"random", 	0,		"kmeans"),
  (100, MSE_TO_CONVERGE, 			60,						"random", 	0,		"kmeans"),
  (100, MSE_TO_CONVERGE_SMALL,	 	20, 					"random", 	0.01	"kmeans"),
  (100, MSE_TO_CONVERGE_SMALL,	 	30, 					"random", 	0,		"kmeans"),
  (100, MSE_TO_CONVERGE_SMALL, 		40, 					"random", 	0,		"kmeans"),
  (100, MSE_TO_CONVERGE_SMALL, 		50, 					"random", 	0,		"kmeans"),
  (100, MSE_TO_CONVERGE_SMALL, 		60,						"random", 	0,		"kmeans"),
  (100, MSE_TO_CONVERGE,	 		20, 					"random", 	-0.11,	"triangle"),
  (100, MSE_TO_CONVERGE,	 		30, 					"random", 	0.04,	"triangle"),
  (100, MSE_TO_CONVERGE, 			40, 					"random", 	0,		"triangle"),
  (100, MSE_TO_CONVERGE, 			50, 					"random", 	0,		"triangle"),
  (100, MSE_TO_CONVERGE, 			60,						"random", 	0,		"triangle"),
  (100, MSE_TO_CONVERGE_SMALL,	 	20, 					"random", 	-0.11	"triangle"),
  (100, MSE_TO_CONVERGE_SMALL,	 	30, 					"random", 	0.04,	"triangle"),
  (100, MSE_TO_CONVERGE_SMALL, 		40, 					"random", 	0,		"triangle"),
  (100, MSE_TO_CONVERGE_SMALL, 		50, 					"random", 	0,		"triangle"),
  (100, MSE_TO_CONVERGE_SMALL, 		60,						"random", 	0,		"triangle"),
  (100, MSE_TO_CONVERGE,	 		20, 					"random", 	0.002,	"enhanced"),
  (100, MSE_TO_CONVERGE,	 		30, 					"random", 	0,		"enhanced"),
  (100, MSE_TO_CONVERGE, 			40, 					"random", 	0,		"enhanced"),
  (100, MSE_TO_CONVERGE, 			50, 					"random", 	0,		"enhanced"),
  (100, MSE_TO_CONVERGE, 			60,						"random", 	0,		"enhanced"),
  (100, MSE_TO_CONVERGE_SMALL,	 	20, 					"random", 	0.002	"enhanced"),
  (100, MSE_TO_CONVERGE_SMALL,	 	30, 					"random", 	0,		"enhanced"),
  (100, MSE_TO_CONVERGE_SMALL, 		40, 					"random", 	0,		"enhanced"),
  (100, MSE_TO_CONVERGE_SMALL, 		50, 					"random", 	0,		"enhanced"),
  (100, MSE_TO_CONVERGE_SMALL, 		60,						"random", 	0,		"enhanced"),
]


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

def outputRuntimes(combination, runtimeDefault, runtimeHeuristic):
	k, kmeansThreshold, centroidsToRemember, seedType, pim, algorithm = combination
	# create the results folder if doesn't exist
	if not os.path.exists(RESULTS_FOLDER):
		os.makedirs(RESULTS_FOLDER)
	# write the runtimes
	timestamp = str(int(time.time()))
	with open(RESULTS_FOLDER + RESULT_BASE_FILENAME + "-" + algorithm + "-" + str(k) + "-" + str(kmeansThreshold) + "-" + str(seedType) + "-" + RESULTS_RUNNER_NAME + "-" + timestamp, 'w') as filehandle:
		filehandle.write(str(buildConbinationLog(combination)))
		filehandle.write("\n")
		filehandle.write(",".join([str(runtime) for runtime in runtimeDefault]))
		filehandle.write("\n")
		filehandle.write(",".join([str(runtime) for runtime in runtimeHeuristic]))

def resolveInitialCentroids(pointList, seedType):
	if seedType == "random": return None
	if seedType == "KPP": return None 		# TODO: Implement KPP handling here

def runHeuristic(pointList, combination):
	# unravel the params
	k, kmeansThreshold, centroidsToRemember, seedType, pim, algorithm = combination
	# calculate the MSE for heuristic from PIM
	kmeansThresholdWithPIM = kmeansThreshold + kmeansThreshold*pim
	initialCentroids = resolveInitialCentroids(pointList, seedType)
	# set additional heuristic specific parameters
	repetitionsRun = 0
	timeTakenHeur = []
	while repetitionsRun < REPETITION_COUNT:
		start_time = time.time()
		# select and run proper algorithm variant
		if algorithm == "kmeans":
			heur_kmeans.Kmeans(k, pointList, kmeansThresholdWithPIM, centroidsToRemember, initialCentroids)
		elif  algorithm == "triangle":
			heur_inequality.Kmeans(k, pointList, kmeansThresholdWithPIM, centroidsToRemember, initialCentroids)
		elif algorithm == "enhanced":
			heur_enhanced.Kmeans(k, pointList, kmeansThresholdWithPIM, centroidsToRemember, initialCentroids)
		else:
			raise Exception("Unknown algorithm " + algorithm)

		timeTakenHeur.append(time.time() - start_time)
		repetitionsRun += 1

	print "Done running the HEURISTIC approach"
	return timeTakenHeur


def runNonHeuristic(pointList, combination):
	# unravel the params
	k, kmeansThreshold, centroidsToRemember, seedType, pim, algorithm = combination
	initialCentroids = resolveInitialCentroids(pointList, seedType)

	repetitionsRun = 0
	timeTakenDefault = []

	while repetitionsRun < REPETITION_COUNT:
		start_time = time.time()

		# select and run proper algorithm variant
		if algorithm == "kmeans":
			def_kmeans.Kmeans(k, pointList, kmeansThreshold, initialCentroids)
		elif  algorithm == "triangle":
			def_inequality.Kmeans(k, pointList, kmeansThreshold, initialCentroids)
		elif algorithm == "enhanced":
			def_enhanced.Kmeans(k, pointList, kmeansThreshold, initialCentroids)
		else:
			raise Exception("Unknown algorithm " + algorithm)

		timeTakenDefault.append(time.time() - start_time)
		repetitionsRun += 1

	print "Done running the NON-HEURISTIC approach"
	return timeTakenDefault

def buildConbinationLog(combination):
	k, kmeansThreshold, centroidsToRemember, seedType, pim, algorithm = combination
	return "k=", k, "MSE", kmeansThreshold, "k'=", centroidsToRemember, "seedType=", seedType, "PIM=", pim, "algorithm=", algorithm


def logExperimentConfiguration(combination):
	print("Running with", buildConbinationLog(combination))

def runExperimentWithConfiguration(pointList, combination):
	# print which experiment is being run
	logExperimentConfiguration(combination)
	# run non-heuristic solution
	timeTakenDefault = runNonHeuristic(pointList, combination)
	# run heuristic solution
	timeTakenHeur = runHeuristic(pointList, combination)
	# output the runtimes
	outputRuntimes(combination, timeTakenDefault, timeTakenHeur)

def guardValidRunner():
	if RESULTS_RUNNER_NAME == "NONE":
		raise Exception("Set your name in RESULTS_RUNNER_NAME variable!")

# ensure that the runnername was set
guardValidRunner()

# load the dataset
pointList = readBirchDataset()


for combination in parameterCombinations:
	runExperimentWithConfiguration(pointList, combination)