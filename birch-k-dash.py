# custom helper classes
from util.datasetloader import * 
from util.experimentrunner import *
from util.guards import *


# repetition configuration
REPETITION_COUNT = 10
MSE_TO_CONVERGE = 5 * pow(10, 13)
MSE_TO_CONVERGE_SMALL = 4.75 * pow(10, 13)

RESULTS_RUNNER_NAME = "NONE"
RESULT_BASE_FILENAME = "birch-"

# experiment parameter combinations
parameterCombinations = [
    # (k, 	kmeansThreshold, 			centroidsToRemember, 	seedType, 	PIM,	algorithm)
    (100, MSE_TO_CONVERGE, 20, "random", 0.01, "kmeans"),
    (100, MSE_TO_CONVERGE, 30, "random", 0, "kmeans"),
    (100, MSE_TO_CONVERGE, 40, "random", 0, "kmeans"),
    (100, MSE_TO_CONVERGE, 50, "random", 0, "kmeans"),
    (100, MSE_TO_CONVERGE, 60, "random", 0, "kmeans"),
    # (100, MSE_TO_CONVERGE_SMALL, 20, "random", 0.01, "kmeans"),
    # (100, MSE_TO_CONVERGE_SMALL, 30, "random", 0, "kmeans"),
    # (100, MSE_TO_CONVERGE_SMALL, 40, "random", 0, "kmeans"),
    # (100, MSE_TO_CONVERGE_SMALL, 50, "random", 0, "kmeans"),
    # (100, MSE_TO_CONVERGE_SMALL, 60, "random", 0, "kmeans"),
    (100, MSE_TO_CONVERGE, 20, "random", -0.11, "triangle"),
    (100, MSE_TO_CONVERGE, 30, "random", 0.04, "triangle"),
    (100, MSE_TO_CONVERGE, 40, "random", 0, "triangle"),
    (100, MSE_TO_CONVERGE, 50, "random", 0, "triangle"),
    (100, MSE_TO_CONVERGE, 60, "random", 0, "triangle"),
    # (100, MSE_TO_CONVERGE_SMALL, 20, "random", -0.11, "triangle"),
    # (100, MSE_TO_CONVERGE_SMALL, 30, "random", 0.04, "triangle"),
    # (100, MSE_TO_CONVERGE_SMALL, 40, "random", 0, "triangle"),
    # (100, MSE_TO_CONVERGE_SMALL, 50, "random", 0, "triangle"),
    # (100, MSE_TO_CONVERGE_SMALL, 60, "random", 0, "triangle"),
    (100, MSE_TO_CONVERGE, 20, "random", 0.002, "enhanced"),
    (100, MSE_TO_CONVERGE, 30, "random", 0, "enhanced"),
    (100, MSE_TO_CONVERGE, 40, "random", 0, "enhanced"),
    (100, MSE_TO_CONVERGE, 50, "random", 0, "enhanced"),
    (100, MSE_TO_CONVERGE, 60, "random", 0, "enhanced"),
    # (100, MSE_TO_CONVERGE_SMALL, 20, "random", 0.002, "enhanced"),
    # (100, MSE_TO_CONVERGE_SMALL, 30, "random", 0, "enhanced"),
    # (100, MSE_TO_CONVERGE_SMALL, 40, "random", 0, "enhanced"),
    # (100, MSE_TO_CONVERGE_SMALL, 50, "random", 0, "enhanced"),
    # (100, MSE_TO_CONVERGE_SMALL, 60, "random", 0, "enhanced")
# KPP seeded experiments
	  (100, MSE_TO_CONVERGE, 20, "KPP", 0, "kmeans"),
	  (100, MSE_TO_CONVERGE_SMALL, 20, "KPP", 0, "kmeans")
]

# ensure that the runnername was set
guardValidRunner(RESULTS_RUNNER_NAME)

# load the dataset
dataset = loadBirchDataset()

# run all experiments
for combination in parameterCombinations:
    runExperimentWithConfiguration(dataset, combination, REPETITION_COUNT)