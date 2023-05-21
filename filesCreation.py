from datetime import datetime
# saving the csv files and the plot images
def filesCreation():
    counter = 1
    #for renaming each time is runt the csv files and the plot images
    csv =  "csvFiles/generation" + datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".csv"
    figName = "plotFigures/plot" + datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".png"
    counter += 1
    
    return csv, figName