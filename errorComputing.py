import numpy as np


import numpy as np

def errorComputing(centroids, realCenters):
    totalError = 0
    minError = float('inf')
    maxError = float('-inf')
    
    for i, centroid in enumerate(centroids):
        # compute the distance of the centroid to each of the real centers        
        distances = [np.linalg.norm(centroid - np.array(realCenter)) for realCenter in realCenters]
        # distance of the centroid to the closest real center
        distanceToRealCenter = min(distances) 
        totalError += distanceToRealCenter
        minError = min(minError, distanceToRealCenter)
        maxError = max(maxError, distanceToRealCenter)
         
    return totalError, minError, maxError



