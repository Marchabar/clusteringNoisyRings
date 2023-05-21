import numpy as np
import scipy.spatial.distance as sc

# Function for recognizing the centers of the circles plotted in dataGenerator.py
def recognizingCircles(allPoints, numberCirc,m = 1.1, maxIter=300, error=1e-5):
    
    initialPoints = np.array(allPoints)
    numberDataPoints = initialPoints.shape[0] # number of data points
    numberCoordinates = initialPoints.shape[1] # number of coordinates of each point

    # randomly initialize membership matrix
    memberships = np.random.rand(numberDataPoints, numberCirc)
    # normalizing the membership matrix so each row sums 1
    memberships = memberships / np.sum(memberships, axis=1, keepdims=True)
        
    # iterate until convergence or max iterations
    for i in range(maxIter):
        # initialize centroids (row, col)
        centroids = np.zeros((numberCirc, numberCoordinates))
        # initialize distances (row, col)
        distances = np.zeros((numberDataPoints, numberCirc))
        for k in range(numberCirc):
            # compute centroids for each circumference
            # numerator: sum of all the points to the power of m times the membership matrix column of that circumference
            # denominator: sum of the  membership matrix colummn for this circumference to the power of m 
           centroids[k] = np.sum(memberships[:, k:k+1] ** m * initialPoints, axis=0) / np.sum(memberships[:, k:k+1] ** m)
           
        # compute ecuclidean distances between each center and each point using cdist 
        distances = sc.cdist(initialPoints, centroids, metric='euclidean')
            
        
        radiusesCentroids = np.zeros(numberCirc)
        # computes radius for each cirummference by computing the weighted average of the distances between the points and the center
        for k in range(numberCirc):
            radiusesCentroids[k] = np.sum(distances[:, k:k+1] * memberships[:, k:k+1]) / np.sum(memberships[:, k:k+1])
        
        
                        

        # update membership matrix with fuzzy c means formula
        membershipsNew = 1 / (distances ** (2 / (m - 1)))
        # normalizing the new membership matrix so each row sums 1
        membershipsNew = membershipsNew / np.sum(membershipsNew, axis=1, keepdims=True)

        # check for convergence calculating the euclidean differences between the new and the old membership matrix
        if np.linalg.norm(membershipsNew - memberships) < error:
            break

        # update membership matrix
        memberships = membershipsNew

    
    return centroids, radiusesCentroids
    

    


