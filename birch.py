# custom helper classes
from util.datasetloader import * 
from util.experimentrunner import *
from util.guards import *


# repetition configuration
REPETITION_COUNT = 1
MSE_TO_CONVERGE = 3
# MSE_TO_CONVERGE_SMALL = 4.75 * pow(10, 13)

RESULTS_RUNNER_NAME = "NONE"
RESULT_BASE_FILENAME = "birch-"

# experiment parameter combinations
parameterCombinations_table2 = [
    # (k, 	kmeansThreshold, 			centroidsToRemember, 	seedType, 	PIM,	algorithm)
# random seeded experiments
    # (100, MSE_TO_CONVERGE, 20, "random", 0.01, "kmeans"),
    # (100, MSE_TO_CONVERGE, 30, "random", 0, "kmeans"),
    # (100, MSE_TO_CONVERGE, 40, "random", 0, "kmeans"),
    # (100, MSE_TO_CONVERGE, 50, "random", 0, "kmeans"),
    # (100, MSE_TO_CONVERGE, 60, "random", 0, "kmeans"),
    (100, MSE_TO_CONVERGE, 20, "random", -0.11, "triangle"),
    (100, MSE_TO_CONVERGE, 30, "random", 0.04, "triangle"),
    (100, MSE_TO_CONVERGE, 40, "random", 0, "triangle"),
    (100, MSE_TO_CONVERGE, 50, "random", 0, "triangle"),
    (100, MSE_TO_CONVERGE, 60, "random", 0, "triangle"),
    # (100, MSE_TO_CONVERGE, 20, "random", 0.002, "enhanced"),
    # (100, MSE_TO_CONVERGE, 30, "random", 0, "enhanced"),
    # (100, MSE_TO_CONVERGE, 40, "random", 0, "enhanced"),
    # (100, MSE_TO_CONVERGE, 50, "random", 0, "enhanced"),
    # (100, MSE_TO_CONVERGE, 60, "random", 0, "enhanced"),
# KPP seeded experiments
	# (100, MSE_TO_CONVERGE, 20, "KPP", 0, "kmeans"),
 #    (100, MSE_TO_CONVERGE, 30, "KPP", 0, "kmeans"),
 #    (100, MSE_TO_CONVERGE, 40, "KPP", 0, "kmeans"),
 #    (100, MSE_TO_CONVERGE, 50, "KPP", 0, "kmeans"),
 #    (100, MSE_TO_CONVERGE, 60, "KPP", 0, "kmeans"),
    (100, MSE_TO_CONVERGE, 20, "KPP", 0, "triangle"),
    (100, MSE_TO_CONVERGE, 30, "KPP", 0, "triangle"),
    (100, MSE_TO_CONVERGE, 40, "KPP", 0, "triangle"),
    (100, MSE_TO_CONVERGE, 50, "KPP", 0, "triangle"),
    (100, MSE_TO_CONVERGE, 60, "KPP", 0, "triangle"),
    # (100, MSE_TO_CONVERGE, 20, "KPP", 0.002, "enhanced"),
    # (100, MSE_TO_CONVERGE, 30, "KPP", 0, "enhanced"),
    # (100, MSE_TO_CONVERGE, 40, "KPP", 0, "enhanced"),
    # (100, MSE_TO_CONVERGE, 50, "KPP", 0, "enhanced"),
    # (100, MSE_TO_CONVERGE, 60, "KPP", 0, "enhanced"),
    ]

parameterCombinations_table3 = [
    # (k, 	kmeansThreshold, 			centroidsToRemember, 	seedType, 	PIM,	algorithm)
    (50, MSE_TO_CONVERGE, 20, "random", 0.31, "triangle"),
    (100, MSE_TO_CONVERGE, 30, "random", 0, "triangle"),
    (500, MSE_TO_CONVERGE, 40, "random", 0, "triangle"),
    (1000, MSE_TO_CONVERGE, 50, "random", 0, "triangle"),
    
    (50, MSE_TO_CONVERGE, 20, "KPP", 0, "triangle"),
    (100, MSE_TO_CONVERGE, 30, "KPP", 0, "triangle"),
    (500, MSE_TO_CONVERGE, 40, "KPP", 0, "triangle"),
    (1000, MSE_TO_CONVERGE, 50, "KPP", 0, "triangle"),
]

# aggregate the parameter combinations
parameterCombinations = parameterCombinations_table2 + parameterCombinations_table3

# ensure that the runnername was set
guardValidRunner(RESULTS_RUNNER_NAME)

# load the dataset
dataset = loadBirchDataset()

# run all experiments
for combination in parameterCombinations:
    runExperimentWithConfiguration(dataset, combination, REPETITION_COUNT, RESULTS_RUNNER_NAME, RESULT_BASE_FILENAME)