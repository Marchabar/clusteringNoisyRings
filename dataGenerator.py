import random
import matplotlib.pyplot as plt
import numpy as np



def dataGenerator(numberCirc, numberPoints, noisePercentage, csv):
    circData = []

    xCoords = []
    yCoords = []

    noisePoints = round(numberPoints * noisePercentage/100)
    remainingPoints = numberPoints - noisePoints

    pointsPerCircInteger = remainingPoints // numberCirc  # to compute integer division
    extraPoints = remainingPoints % numberCirc

    for i in range(numberCirc):
        pointsPerCirc = pointsPerCircInteger + (extraPoints > 0)
        extraPoints -= 1
        # with the circData we have the number of points for each of the circunferences in a list
        circData.append(pointsPerCirc)
    # realCenters is a list with the real centers of the circles for later computing the errors
    realCenters = []
    for i in range(numberCirc):
        numPoints = circData[i]
        radius = random.uniform(3, 8)
        xCenter = random.uniform(-0, 100)
        yCenter = random.uniform(-0, 100)
        realCenters.append([xCenter, yCenter])
        angle = []
        a = 0  # is the angle counter for the points of this circunference, that is why we sum it below again
        for j in range(numPoints):
            # Randomly adjust the angle between points
            a += random.uniform(0.7, 1.3)
            # list with all the angles of all the points for this circumference, of course between 0 and 2pi
            angle.append(a)

        # for getting the x and y coordinates of each point for this circunference
        xFin = xCenter + radius * np.cos(angle)
        yFin = yCenter + radius * np.sin(angle)

        xCoords.extend(xFin)
        yCoords.extend(yFin)
        


    # for adding the noise points randomly
    xNoise = []
    yNoise = []
    for i in range(noisePoints):
        x = random.uniform(-0, 100)
        y = random.uniform(-0, 100)

        xCoords.append(x)
        yCoords.append(y)

        xNoise.append(x)
        yNoise.append(y)
    

    # getting all the plotted points in a list of lists
    allPoints = []
    for i in range(len(xCoords)):
        allPoints.append([xCoords[i], yCoords[i]])
        
    
    
    res = np.asarray(allPoints)
    np.savetxt(csv, res, delimiter=",")
    

    return allPoints, realCenters