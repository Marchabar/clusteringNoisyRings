import csv
import os

def addRowToTable(filename, numCircumferences, numPoints, noisePercentage, totalError, minError, maxError):
    # to generate a csv with all the data of each execution
    
    row = [numCircumferences, numPoints, noisePercentage, totalError, minError, maxError]
    
    # to check if the file exists and to skip the first line of the csv since it is the header
    file_exists = os.path.isfile(filename)
    
    with open(filename, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        
        # Skip writing the row if the file exists and it has a non-zero size (first line)
        if file_exists and csvfile.tell() == 0:
            return
        
        writer.writerow(row)

