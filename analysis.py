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

sepal_length_hist= iris["sepal_length"].hist(color="darkgreen", alpha=0.7)  # isolates sepal length column
#setosa["sepal_length"].hist()
#versicolor["sepal_length"].hist()
#virginica["sepal_length"].hist()
plt.xlabel("Length in mm") # Adds a label to the x axis
plt.ylabel("Frequency")
plt.title("Histogram of Sepal Lengths") # Adds a title to the histogram
plt.savefig("sepal_length_hist.png")          # saves the histogram to a PNG file
#plt.show()  # displays the histogram when the program is run

sepal_width_hist= iris["sepal_width"].hist(color="darkgreen", alpha=0.7)
plt.xlabel("Length in mm") 
plt.ylabel("Frequency")
plt.title("Histogram of Sepal Widths")  
plt.savefig("sepal_width_hist.png")
#plt.show() 

petal_length_hist= iris["petal_length"].hist(color="#5E47CB") # hexadecimal colour of random iris flower
plt.xlabel("Length in mm") 
plt.ylabel("Frequency")
plt.title("Histogram of Petal Lengths")  
plt.savefig("petal_length_hist.png")
#plt.show() 

petal_width_hist= iris["petal_width"].hist(color="#5E47CB")
plt.xlabel("Length in mm") 
plt.ylabel("Frequency")
plt.title("Histogram of Petal Widths")  
plt.savefig("petal_width_hist.png")
#plt.show() 

fig1, axes1= plt.subplots(nrows=1, ncols=3, figsize=(8, 5)) # Creates a four histogram plot, number of rows and columns specified and the size of the figure in inches
setosa["sepal_length"].hist(ax=axes1[0], color= "darkgreen", alpha=0.8)
axes1[0].set_title("Setosa Sepal Length")

versicolor["sepal_length"].hist(ax=axes1[1], color= "darkgreen", alpha=0.75)
axes1[1].set_title("Versicolor Sepal Length")

virginica["sepal_length"].hist(ax=axes1[2], color= "darkgreen", alpha=0.7)
axes1[2].set_title("Virginica Sepal Length")
plt.savefig("sepal_length_comparison.png")
#plt.show()

fig2, axes2= plt.subplots(nrows=1, ncols=3, figsize=(8,5))
setosa["sepal_width"].hist(ax=axes2[0], color= "darkgreen", alpha=0.8)
axes2[0].set_title("Setosa Sepal Width")

versicolor["sepal_width"].hist(ax=axes2[1], color= "darkgreen", alpha=0.75)
axes2[1].set_title("Versicolor Sepal Width")

virginica["sepal_width"].hist(ax=axes2[2], color= "darkgreen", alpha=0.7)
axes2[2].set_title("Virginica Sepal Width")
plt.savefig("sepal_width_comparison.png")
#plt.show()

fig3, axes3= plt.subplots(nrows=1, ncols=3, figsize=(8,5))
setosa["petal_length"].hist(ax=axes3[0], color="#5E47CB", alpha=0.8)
axes3[0].set_title("Setosa Petal Length")

versicolor["petal_length"].hist(ax=axes3[1], color="#5E47CB", alpha=0.75)
axes3[1].set_title("Versicolor Petal Length")

virginica["petal_length"].hist(ax=axes3[2], color="#5E47CB", alpha=0.7)
axes3[2].set_title("Virginica Petal Length")
plt.savefig("petal_length_comparison.png")
#plt.show()

fig4, axes4= plt.subplots(nrows=1, ncols=3, figsize=(8,5))
setosa["petal_width"].hist(ax=axes4[0], color="#5E47CB", alpha=0.8)
axes4[0].set_title("Setosa Petal Width")

versicolor["petal_width"].hist(ax=axes4[1], color="#5E47CB", alpha=0.75)
axes4[1].set_title("Versicolor Petal Width")

virginica["petal_width"].hist(ax=axes4[2], color="#5E47CB", alpha=0.7)
axes4[2].set_title("Virginica Petal Width")
plt.savefig("petal_width_comparison.png")
plt.show()