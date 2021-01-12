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

def calculateThresholdWithPim(nonHeuristicError, pim):
    return nonHeuristicError + (nonHeuristicError*pim)/100

def runHeuristic(pointList, combination, nonHeuristicError, initialCentroids):
    # unravel the params
    k, kmeansThreshold, centroidsToRemember, seedType, pim, algorithm = combination
    # calculate the absolute MSE for heuristic from PIM
    kmeansThresholdWithPIM = calculateThresholdWithPim(nonHeuristicError, pim)

    print "Error to beat:", kmeansThresholdWithPIM, "nonHeurError:", nonHeuristicError, "PIM:", pim

    start_time = time.time()
    # select and run proper algorithm variant
    if algorithm == "kmeans":
        heur_kmeans.Kmeans(k, pointList, kmeansThresholdWithPIM, centroidsToRemember, initialCentroids)
    elif algorithm == "triangle":
        # this code was modified to take kmeansThresholdWithPIM as ABSOLUTE error
        heur_inequality.Kmeans(k, pointList, kmeansThresholdWithPIM, centroidsToRemember, initialCentroids)
    elif algorithm == "enhanced":
        heur_enhanced.Kmeans(k, pointList, kmeansThresholdWithPIM, centroidsToRemember, initialCentroids)
    else:
        raise Exception("Unknown algorithm " + algorithm)
    timeTakenHeur = time.time() - start_time

    print "Done running the HEURISTIC approach"
    return timeTakenHeur


def runNonHeuristic(pointList, combination, initialCentroids):
    # unravel the params
    k, kmeansThreshold, centroidsToRemember, seedType, pim, algorithm = combination
    start_time = time.time()

    # select and run proper algorithm variant
    if algorithm == "kmeans":
        impl = def_kmeans.Kmeans(k, pointList, kmeansThreshold, initialCentroids)
        nonHeuristicError = impl.error
    elif algorithm == "triangle":
        impl = def_inequality.Kmeans(k, pointList, kmeansThreshold, initialCentroids)
        nonHeuristicError = impl.error
    elif algorithm == "enhanced":
        impl = def_enhanced.Kmeans(k, pointList, kmeansThreshold, initialCentroids)
        nonHeuristicError = impl.error
    else:
        raise Exception("Unknown algorithm " + algorithm)

    timeTakenDefault = time.time() - start_time

    print
    "Done running the NON-HEURISTIC approach"
    return timeTakenDefault, nonHeuristicError


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
    repetitionsRun = 0
    timeTakenDefault = []
    timeTakenHeur = []

    while repetitionsRun < repetitions:
        # find centroids for this replicate
        initialCentroids = resolveInitialCentroids(pointList, seedType, k)

        # run non-heuristic solution
        timeNonHeur,nonHeuristicError  = runNonHeuristic(pointList, combination, initialCentroids)
        timeTakenDefault.append(timeNonHeur)

        # run heuristic solution
        timeHeur = runHeuristic(pointList, combination, nonHeuristicError, initialCentroids)
        timeTakenHeur.append(timeHeur)
        repetitionsRun += 1
    
    # output the runtimes
    outputRuntimes(combination, timeTakenDefault, timeTakenHeur, runnerName, resultFilename)

