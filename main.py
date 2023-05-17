from inputData import inputData
from dataGenerator import dataGenerator
from clusterComputing import recognizingCircles
from filesCreation import filesCreation
from errorComputing import errorComputing
from plotResults import plotResults
from tableGenerator import addRowToTable

numberCirc, numberPoints, noisePercentage = inputData()
csv, figName = filesCreation()
allPoints, realCenters = dataGenerator(numberCirc, numberPoints, noisePercentage, csv)
centroids, radiusesCentroids = recognizingCircles(allPoints, numberCirc)
totalError,minError,maxError = errorComputing(centroids, realCenters)
addRowToTable("table.csv", numberCirc, numberPoints, noisePercentage, totalError, minError, maxError)
plotResults(totalError,minError,maxError, centroids, csv, numberCirc, noisePercentage, numberPoints, figName, radiusesCentroids)
