from tkinter import messagebox
from tkinter import *

def inputData():
    def submitInput():
        global numberCirc, numberPoints, noisePercentage
    
        # get values from entries
        numberCirc = int(circlesInput.get())
        numberPoints = int(pointsInput.get())
        noisePercentage = float(noiseInput.get())

        # check if inputs are valid
        if not (1 <= numberCirc <= 10):
            messagebox.showerror("Error", "Invalid input for number of circles. Please enter an integer between 1 and 10.")
            return
        if not (1 <= numberPoints <= 6000):
            messagebox.showerror("Error", "Invalid input for number of points. Please enter an integer between 1 and 6000.")
            return
        if not (1.00 <= noisePercentage <= 10.00):
            messagebox.showerror("Error", "Invalid input for percentage of noise. Please enter a float between 1.00 and 10.00.")
            return

        # close the window
        root.destroy()

    #tkinter implementation to get the input from the user and to design the window
    root = Tk()
    root.title("Circle Recognition")
    root.geometry("400x200")

    circlesLabel = Label(root, text="Enter the number of circles (1-10):")
    circlesLabel.grid(row=0, column=0, padx=10, pady=10)
    circlesInput = Entry(root)
    circlesInput.grid(row=0, column=1, padx=10, pady=10)

    pointsLabel = Label(root, text="Enter the number of points (1-6000):")
    pointsLabel.grid(row=1, column=0, padx=10, pady=10)
    pointsInput = Entry(root)
    pointsInput.grid(row=1, column=1, padx=10, pady=10)

    noiseLabel = Label(root, text="Enter the percentage of noise (1-10):")
    noiseLabel.grid(row=2, column=0, padx=10, pady=10)
    noiseInput = Entry(root)
    noiseInput.grid(row=2, column=1, padx=10, pady=10)

    submit_button = Button(root, text="Submit", command=submitInput)
    submit_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    root.mainloop()

    return numberCirc, numberPoints, noisePercentage
