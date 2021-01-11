import pandas as pd
import numpy as np
import cPickle as pickle



# input dataset configuration
DATASET_BASE_LOCATION = "originalrepo/Dataset/"
DATASET_NAME_BIRCH = 'birch.txt'
DATASET_NAME_COVTYPE = 'covtype.data'
DATASET_NAME_CUP = 'cup98LRN.txt'
DATASET_NAME_SYNTHETIC = "synthetic"
DATASET_NAME_MNIST = "mnist768"


OBSERVATION_PRINT_THRESHOLD = 1000


def guardDimensionality(point, dimensionality):
    if len(point) != dimensionality:
        raise Exception("Unexpected point length!")
        print(point)
        print(len(point))


def loadMnistDataset():
    dimensionality = 784
    pointList = []
    observationsLoaded = 0
    # open file and read the content in a list
    with open(DATASET_BASE_LOCATION + DATASET_NAME_MNIST, 'r') as filehandle:
        for line in filehandle:
            # remove linebreak which is the last character of the string
            currentPointString = line[:-1]
            # parse the points
            currentPoint = currentPointString.split(",")
            # convert to numbers
            point = [float(point) for point in currentPoint if point != '']
            # ensure point of correct size was extracted
            guardDimensionality(point, dimensionality)
            # add item to the list
            pointList.append(point)
            observationsLoaded += 1
            if not len(pointList)%OBSERVATION_PRINT_THRESHOLD: print("Loaded", observationsLoaded, "observations")
    print("Dataset loaded with", len(pointList), "observations")
    return pointList

def loadBirchDataset():
    dimensionality = 2
    pointList = []
    # open file and read the content in a list
    with open(DATASET_BASE_LOCATION + DATASET_NAME_BIRCH, 'r') as filehandle:
        for line in filehandle:
            # remove linebreak which is the last character of the string
            currentPointString = line[:-1]
            # parse the points
            currentPoint = currentPointString.split("    ")
            # convert to numbers
            point = [int(point) for point in currentPoint if point != '']
            guardDimensionality(point, dimensionality)
            # add item to the list
            pointList.append(point)

    return pointList

def loadcovtype():
    dimensionality = 55
    data = []
    linesRead = 0
    with open(DATASET_BASE_LOCATION + DATASET_NAME_COVTYPE,"r") as inputFile:
        for line in inputFile:
            # read 150k lines implicitly
            if linesRead == 150000:
                break
            point = [float(x) for x in line.strip().split(",")]
            guardDimensionality(point, dimensionality)
            data.append(point)
            linesRead += 1
    return data


def loadcovtypeP3():
    dimensionality = 55
    data = []
    with open(DATASET_BASE_LOCATION + DATASET_NAME_COVTYPE,"r", low_memory=False) as inputFile:
        for line in inputFile:
            # read 150k lines implicitly
            if linesRead == 150000:
                break
            point = [float(x) for x in line.strip().split(",")]
            guardDimensionality(point, dimensionality)
            data.append(point)
    return data


def loadCupDataset():
    data = []
    data = pd.read_csv(DATASET_BASE_LOCATION + DATASET_NAME_CUP, low_memory=False)
    data = data.fillna(0)

    cat_columns = data.select_dtypes([np.object]).columns
    for col in cat_columns:
        data[col] = data[col].astype('category')

    cat_columns = data.select_dtypes(['category']).columns
    data[cat_columns] = data[cat_columns].apply(lambda x: x.cat.codes)

    pointList = data.values.tolist()

    return pointList


def readSyntheticDataset():
    with open(DATASET_BASE_LOCATION + DATASET_NAME_SYNTHETIC, "rb") as f:
        numpyPointList = pickle.load(f)
    return numpyPointList.tolist()
