# custom helper classes
from util.datasetloader import * 
from util.experimentrunner import *
from util.guards import *

# repetition configuration
REPETITION_COUNT = 10
MSE_TO_CONVERGE = 1

RESULTS_RUNNER_NAME = "TEST"
RESULT_BASE_FILENAME = "cup-"

# experiment parameter combinations
parameterCombinations_table2 = [
    # (k, 	kmeansThreshold, 			centroidsToRemember, 	seedType, 	PIM,	algorithm)
# random seeded
    (100, MSE_TO_CONVERGE, 20, "random", 0.81, "triangle"),
    (100, MSE_TO_CONVERGE, 30, "random", 0.11, "triangle"),
    (100, MSE_TO_CONVERGE, 40, "random", 0.08, "triangle"),
    (100, MSE_TO_CONVERGE, 50, "random", -0.18, "triangle"),
    (100, MSE_TO_CONVERGE, 60, "random", 0, "triangle"),

# KPP seeded
    (100, MSE_TO_CONVERGE, 20, "KPP", 0.7, "triangle"),
    (100, MSE_TO_CONVERGE, 30, "KPP", 0.15, "triangle"),
    (100, MSE_TO_CONVERGE, 40, "KPP", 0.02, "triangle"),
    (100, MSE_TO_CONVERGE, 50, "KPP", -0.01, "triangle"),
    (100, MSE_TO_CONVERGE, 60, "KPP", 0, "triangle"),
]

parameterCombinations_table3 = [
    # (k, 	kmeansThreshold, 			centroidsToRemember, 	seedType, 	PIM,	algorithm)
    (50, MSE_TO_CONVERGE, 40, "random", 0.51, "triangle"),
    (100, MSE_TO_CONVERGE, 40, "random", -0.06, "triangle"),
    (500, MSE_TO_CONVERGE, 40, "random", 0, "triangle"),
    (1000, MSE_TO_CONVERGE, 40, "random", 0, "triangle"),
    
    (50, MSE_TO_CONVERGE, 40, "KPP", 0.99, "triangle"),
    (100, MSE_TO_CONVERGE, 40, "KPP", 0.15, "triangle"),
    (500, MSE_TO_CONVERGE, 40, "KPP", 0.03, "triangle"),
    (1000, MSE_TO_CONVERGE, 40, "KPP", 0.02, "triangle"),
]



# aggregate the parameter combinations
parameterCombinations = parameterCombinations_table2 + parameterCombinations_table3

# ensure that the runnername was set
guardValidRunner(RESULTS_RUNNER_NAME)

# load the dataset
dataset = loadCupDataset()

# run all experiments
for combination in parameterCombinations:
    runExperimentWithConfiguration(dataset, combination, REPETITION_COUNT, RESULTS_RUNNER_NAME, RESULT_BASE_FILENAME)

