import os
import time

# output destination configuration
RESULTS_FOLDER = "results/"

def buildConbinationLogText(combination):
    k, kmeansThreshold, centroidsToRemember, seedType, pim, algorithm = combination
    return "k=", k, "MSE", kmeansThreshold, "k'=", centroidsToRemember, "seedType=", seedType, "PIM=", pim, "algorithm=", algorithm

def outputRuntimes(combination, runtimeDefault, runtimeHeuristic, runnerName, datasetName):
    k, kmeansThreshold, centroidsToRemember, seedType, pim, algorithm = combination
    # create the results folder if doesn't exist
    if not os.path.exists(RESULTS_FOLDER):
        os.makedirs(RESULTS_FOLDER)
    # write the runtimes
    with open(RESULTS_FOLDER + datasetName + "-" + algorithm + "-" + str(k) + "-" + str(
            kmeansThreshold) + "-" + str(centroidsToRemember) + "-" + str(seedType), 'w+') as filehandle:
        filehandle.write(runnerName + ":" + str(buildConbinationLogText(combination)))
        filehandle.write("\n")
        for replicate in runtimeDefault:
            filehandle.write("non-heuristic," + str(replicate))
            filehandle.write("\n")
        for replicate in runtimeHeuristic:
            filehandle.write("heuristic," + str(replicate))
            filehandle.write("\n")