import numpy as np


import numpy as np

def errorComputing(centroids, realCenters):
    totalError = 0
    minError = float('inf')
    maxError = float('-inf')
    
    for i, centroid in enumerate(centroids):        
        distances = [np.linalg.norm(centroid - np.array(realCenter)) for realCenter in realCenters]
        distanceToRealCenter = min(distances) # distance of the centroid to the closest real center
        totalError += distanceToRealCenter
        minError = min(minError, distanceToRealCenter)
        maxError = max(maxError, distanceToRealCenter)
         
    return totalError, minError, maxError



