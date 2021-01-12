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
    timestamp = str(int(time.time()))
    with open(RESULTS_FOLDER + datasetName + "-" + algorithm + "-" + str(k) + "-" + str(
            kmeansThreshold) + "-" + str(seedType) + "-" + runnerName + "-" + timestamp, 'w') as filehandle:
        filehandle.write(str(buildConbinationLogText(combination)))
        filehandle.write("\n")
        filehandle.write(",".join([str(runtime) for runtime in runtimeDefault]))
        filehandle.write("\n")
        filehandle.write(",".join([str(runtime) for runtime in runtimeHeuristic]))