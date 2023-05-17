import numpy as np
import matplotlib.pyplot as plt

def plotResults(totalError, minError, maxError, centroids, csv, numberCircle, noisePercentage, numberPoints,  figName, radius):
    # to get the points from initially generated which are in the csv
    npPlotting = np.genfromtxt(csv, delimiter=',')
    
    # create subplots with 1 row and 2 columns
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))
    
    # plot the graph in the first subplot
    axs[0].scatter(npPlotting[:, 0], npPlotting[:, 1], c="red")
    axs[0].scatter(centroids[:, 0], centroids[:, 1], c="black", marker="x")
    for k in range(numberCircle):
        circle = plt.Circle(centroids[k], radius[k], color='black', fill=False)
        axs[0].add_artist(circle)  
    axs[0].set_title("Nº Circumferences: " + str(numberCircle) + "| Nº Points: " + str(numberPoints) + "| Noise: " + str(noisePercentage) + "%")
    axs[0].set_xlim([0, 100])
    axs[0].set_ylim([0, 100])
    axs[0].set_aspect('equal')  # Set equal aspect ratio for x and y axes


    # plot the errors in the second subplot
    errors = [totalError, minError, maxError]
    labels = ['Total Error', 'Minimum Error', 'Maximum Error']
    axs[1].bar(labels, errors)
    axs[1].set_title("Errors")
    # to show every value of the error above the bar
    for i, error in enumerate(errors):
        axs[1].text(i, error, str(error), ha='center', va='bottom')

    # adjust the spacing between subplots
    fig.tight_layout()

    plt.subplots_adjust(left=0.05, bottom=0.1, right=0.99)

    # save the figure
    plt.savefig(figName)

    # show the figure
    plt.show()


