# custom helper classes
from util.datasetloader import * 
from util.experimentrunner import *
from util.guards import *

# repetition configuration
REPETITION_COUNT = 10
MSE_TO_CONVERGE = None

RESULTS_RUNNER_NAME = "NONE"
RESULT_BASE_FILENAME = "synthetic-"



# experiment parameter combinations
parameterCombinations_table2 = [
    # (k, 	kmeansThreshold, 			centroidsToRemember, 	seedType, 	PIM,	algorithm)
# random seeded
    (100, MSE_TO_CONVERGE, 20, "random", 0.19, "triangle"),
    (100, MSE_TO_CONVERGE, 30, "random", 0.11, "triangle"),
    (100, MSE_TO_CONVERGE, 40, "random", 0.06, "triangle"),
    (100, MSE_TO_CONVERGE, 50, "random", 0.03, "triangle"),
    (100, MSE_TO_CONVERGE, 60, "random", 0.01, "triangle"),

# KPP seeded
    (100, MSE_TO_CONVERGE, 20, "KPP", 0.15, "triangle"),
    (100, MSE_TO_CONVERGE, 30, "KPP", 0.08, "triangle"),
    (100, MSE_TO_CONVERGE, 40, "KPP", 0.04, "triangle"),
    (100, MSE_TO_CONVERGE, 50, "KPP", 0.01, "triangle"),
    (100, MSE_TO_CONVERGE, 60, "KPP", 0.01, "triangle"),
]

parameterCombinations_table3 = [
    # (k, 	kmeansThreshold, 			centroidsToRemember, 	seedType, 	PIM,	algorithm)
    (50, MSE_TO_CONVERGE, 20, "random", 0.09, "triangle"),
    (100, MSE_TO_CONVERGE, 30, "random", 0.05, "triangle"),
    (500, MSE_TO_CONVERGE, 40, "random", 0.03, "triangle"),
    (1000, MSE_TO_CONVERGE, 50, "random", 0.01, "triangle"),
    
    (50, MSE_TO_CONVERGE, 20, "KPP", 0.07, "triangle"),
    (100, MSE_TO_CONVERGE, 30, "KPP", 0.04, "triangle"),
    (500, MSE_TO_CONVERGE, 40, "KPP", 0.01, "triangle"),
    (1000, MSE_TO_CONVERGE, 50, "KPP", 0.01, "triangle"),
]



# aggregate the parameter combinations
parameterCombinations = parameterCombinations_table2 + parameterCombinations_table3

# ensure that the runnername was set
guardValidRunner(RESULTS_RUNNER_NAME)

# load the dataset
dataset = readSyntheticDataset()

# run all experiments
for combination in parameterCombinations:
    runExperimentWithConfiguration(dataset, combination, REPETITION_COUNT)