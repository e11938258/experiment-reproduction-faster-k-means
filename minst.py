# custom helper classes
from util.datasetloader import * 
from util.experimentrunner import *
from util.guards import *

# repetition configuration
REPETITION_COUNT = 10
MSE_TO_CONVERGE = None

RESULTS_RUNNER_NAME = "NONE"
RESULT_BASE_FILENAME = "minst-"


# experiment parameter combinations
parameterCombinations_table2 = [
    # (k, 	kmeansThreshold, 			centroidsToRemember, 	seedType, 	PIM,	algorithm)
# random seeded
    (100, MSE_TO_CONVERGE, 20, "random", 1.3, "triangle"),
    (100, MSE_TO_CONVERGE, 30, "random", 0.6, "triangle"),
    (100, MSE_TO_CONVERGE, 40, "random", 0.36, "triangle"),
    (100, MSE_TO_CONVERGE, 50, "random", 0.3, "triangle"),
    (100, MSE_TO_CONVERGE, 60, "random", 0.23, "triangle"),

# KPP seeded
    (100, MSE_TO_CONVERGE, 20, "KPP", 1.36, "triangle"),
    (100, MSE_TO_CONVERGE, 30, "KPP", 0.71, "triangle"),
    (100, MSE_TO_CONVERGE, 40, "KPP", 0.36, "triangle"),
    (100, MSE_TO_CONVERGE, 50, "KPP", 0.18, "triangle"),
    (100, MSE_TO_CONVERGE, 60, "KPP", 0.09, "triangle"),
]

parameterCombinations_table3 = [
    # (k, 	kmeansThreshold, 			centroidsToRemember, 	seedType, 	PIM,	algorithm)
    (50, MSE_TO_CONVERGE, 20, "random", 0.94, "triangle"),
    (100, MSE_TO_CONVERGE, 30, "random", 0.38, "triangle"),
    (500, MSE_TO_CONVERGE, 40, "random", 0.09, "triangle"),
    (1000, MSE_TO_CONVERGE, 50, "random", 0.13, "triangle"),
    
    (50, MSE_TO_CONVERGE, 20, "KPP", 0.87, "triangle"),
    (100, MSE_TO_CONVERGE, 30, "KPP", 0.52, "triangle"),
    (500, MSE_TO_CONVERGE, 40, "KPP", 0.23, "triangle"),
    (1000, MSE_TO_CONVERGE, 50, "KPP", 0.07, "triangle"),
]



# aggregate the parameter combinations
parameterCombinations = parameterCombinations_table2 + parameterCombinations_table3

# ensure that the runnername was set
guardValidRunner(RESULTS_RUNNER_NAME)

# load the dataset
dataset = loadMnistDataset()

# run all experiments
for combination in parameterCombinations:
    runExperimentWithConfiguration(dataset, combination, REPETITION_COUNT, RESULTS_RUNNER_NAME, RESULT_BASE_FILENAME)
