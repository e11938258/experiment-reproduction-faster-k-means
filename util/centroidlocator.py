import numpy as np

import originalrepo.Code.kpp as kpp

def runKPP(pointList, k):
	x = np.array(pointList)
	kplus = kpp.KPP(k, X = x)
	kplus.init_centers()
	cList = [kpp.Point(x, len(x)) for x in kplus.mu]
	return cList

def resolveInitialCentroids(pointList, seedType, k):
    if seedType == "random": return None
    if seedType == "KPP": 
    	return runKPP(pointList, k)
