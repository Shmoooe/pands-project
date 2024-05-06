# This programme will:
# Output a summary of each variable to a single text file,  
# Save a histogram of each variable to png files, and  
# Output a scatter plot of each pair of variables.  
# Author: Joanna Kelly

import pandas as pd    # imports pandas library and assigns the nickname 'pd'

iris = pd.read_csv("iris.csv") # Reads the data from a csv file and stores it in a pandas data frame
description = iris.describe() # This creates summary statistics for each variable


'''
with open("summary_statistics.txt", "w") as file:     # Creates a txt file 
    file.write(description.to_string())         # writes to the new file and converts the summary stats to a string
'''

import matplotlib.pyplot as plt # software to create my histograms and scatter plots

setosa = iris[iris["species"]== "setosa"]  #seperates the species for later analysis
versicolor = iris[iris["species"]== "versicolor"]
virginica = iris[iris["species"]== "virginica"]

iris["sepal_length"].hist()  # isolates sepal length column
#setosa["sepal_length"].hist()
#versicolor["sepal_length"].hist()
#virginica["sepal_length"].hist()
plt.xlabel("Length in mm") # Adds a label to the x axis
plt.ylabel("Frequency")
plt.title("Histogram of Sepal Lengths") # Adds a title to the histogram
plt.savefig("sepal_length_hist.png")          # saves the histogram to a PNG file
plt.show()  # displays the histogram when the program is run

iris["sepal_width"].hist()
plt.xlabel("Length in mm") 
plt.ylabel("Frequency")
plt.title("Histogram of Sepal Widths")  
plt.savefig("sepal_width_hist.png")
plt.show() 
