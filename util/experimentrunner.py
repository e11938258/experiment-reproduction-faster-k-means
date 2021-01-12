import time
import numpy as np

# algorithms under test
import originalrepo.Code.kmeans as def_kmeans
import originalrepo.Code.heuristic_kmeans as heur_kmeans
import originalrepo.Code.triangleInequality as def_inequality
import originalrepo.Code.heuristic_triangleinequality as heur_inequality
import originalrepo.Code.enhancedKmeans as def_enhanced
import originalrepo.Code.heuristic_enhancedKmeans as heur_enhanced


# helper function to generate centroids
from centroidlocator import *
from util.resultwriter import *

def runHeuristic(pointList, combination, repetitions, initialCentroids):
    # unravel the params
    k, kmeansThreshold, centroidsToRemember, seedType, pim, algorithm = combination
    # calculate the MSE for heuristic from PIM
    kmeansThresholdWithPIM = kmeansThreshold + kmeansThreshold * pim
    # set additional heuristic specific parameters
    repetitionsRun = 0
    timeTakenHeur = []
    while repetitionsRun < repetitions:
        start_time = time.time()
        # select and run proper algorithm variant
        if algorithm == "kmeans":
            heur_kmeans.Kmeans(k, pointList, kmeansThresholdWithPIM, centroidsToRemember, initialCentroids)
        elif algorithm == "triangle":
            heur_inequality.Kmeans(k, pointList, kmeansThresholdWithPIM, centroidsToRemember, initialCentroids)
        elif algorithm == "enhanced":
            heur_enhanced.Kmeans(k, pointList, kmeansThresholdWithPIM, centroidsToRemember, initialCentroids)
        else:
            raise Exception("Unknown algorithm " + algorithm)

        timeTakenHeur.append(time.time() - start_time)
        repetitionsRun += 1

    print
    "Done running the HEURISTIC approach"
    return timeTakenHeur


def runNonHeuristic(pointList, combination, repetitions, initialCentroids):
    # unravel the params
    k, kmeansThreshold, centroidsToRemember, seedType, pim, algorithm = combination

    repetitionsRun = 0
    timeTakenDefault = []

    while repetitionsRun < repetitions:
        start_time = time.time()

        # select and run proper algorithm variant
        if algorithm == "kmeans":
            def_kmeans.Kmeans(k, pointList, kmeansThreshold, initialCentroids)
        elif algorithm == "triangle":
            def_inequality.Kmeans(k, pointList, kmeansThreshold, initialCentroids)
        elif algorithm == "enhanced":
            def_enhanced.Kmeans(k, pointList, kmeansThreshold, initialCentroids)
        else:
            raise Exception("Unknown algorithm " + algorithm)

        timeTakenDefault.append(time.time() - start_time)
        repetitionsRun += 1

    print
    "Done running the NON-HEURISTIC approach"
    return timeTakenDefault


def buildConbinationLog(combination):
    k, kmeansThreshold, centroidsToRemember, seedType, pim, algorithm = combination
    return "k=", k, "MSE", kmeansThreshold, "k'=", centroidsToRemember, "seedType=", seedType, "PIM=", pim, "algorithm=", algorithm


def logExperimentConfiguration(combination):
    print("Running with", buildConbinationLog(combination))


def runExperimentWithConfiguration(pointList, combination, repetitions, runnerName, resultFilename):
    # print which experiment is being run
    logExperimentConfiguration(combination)

    # find the centroids
    k, kmeansThreshold, centroidsToRemember, seedType, pim, algorithm = combination
    initialCentroids = resolveInitialCentroids(pointList, seedType, k)

    # run non-heuristic solution
    timeTakenDefault = runNonHeuristic(pointList, combination, repetitions, initialCentroids)
    # run heuristic solution
    timeTakenHeur = runHeuristic(pointList, combination, repetitions, initialCentroids)
    # output the runtimes
    outputRuntimes(combination, timeTakenDefault, timeTakenHeur, runnerName, resultFilename)