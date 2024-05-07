# This programme will:
# Output a summary of each variable to a single text file,  
# Save a histogram of each variable to png files, and  
# Output a scatter plot of each pair of variables.  
# Author: Joanna Kelly

import pandas as pd    # imports pandas library and assigns the nickname 'pd'

iris = pd.read_csv("iris.csv") # Reads the data from a csv file and stores it in a pandas data frame
description = iris.describe() # This creates summary statistics for each variable

with open("summary_statistics.txt", "w") as file:     # Creates a txt file 
    file.write(description.to_string())         # writes to the new file and converts the summary stats to a string

import matplotlib.pyplot as plt # software to create my histograms and scatter plots

setosa = iris[iris["species"]== "setosa"]  #seperates the species for later analysis
versicolor = iris[iris["species"]== "versicolor"]
virginica = iris[iris["species"]== "virginica"]


fig, axes= plt.subplots(nrows=2, ncols=2, figsize=(10, 6)) # Creates a four histogram plot, number of rows and columns specified and the size of the figure in inches
iris["sepal_length"].hist(ax=axes[0,0], color="darkgreen", alpha=0.7)  # isolates sepal length column and assigns it to row 1, column 1, alpha refers to the opacity
axes[0,0].set_xlabel("Length in mm") # labels the x axis, along the bottom
axes[0,0].set_ylabel("Frequency") # labels the y axis, up the side
axes[0,0].set_title("Sepal Length") # gives a title to this individual histogram
plt.subplots_adjust(bottom=0.15) # adjusts the spacing between the margins of the subplots so that x axis labels do not overlap with the titles of the next subplots

iris["sepal_width"].hist(ax=axes[0,1], color="darkgreen", alpha=0.7)
axes[0,1].set_xlabel("Width in mm")
axes[0,1].set_ylabel("Frequency")
axes[0,1].set_title("Sepal Width")
plt.subplots_adjust(bottom=0.15) # adjusts the spacing between the margins of the subplots so that x axis labels do not overlap with the titles of the next subplots

iris["petal_length"].hist(ax=axes[1,0], color="#5E47CB") # hexadecimal colour of random iris flower
axes[1,0].set_xlabel("Length in mm")
axes[1,0].set_ylabel("Frequency")
axes[1,0].set_title("Petal Length")

iris["petal_width"].hist(ax=axes[1,1], color="#5E47CB", alpha= 0.8)
axes[1,1].set_xlabel("Width in mm")
axes[1,1].set_ylabel("Frequency")
axes[1,1].set_title("Petal Width")
plt.tight_layout  # prevents overlapping of subplots
plt.savefig("variable_overview_hist.png")          # saves the histogram to a PNG file
plt.show()  # displays the histogram when the program is run



fig1, axes1= plt.subplots(nrows=1, ncols=3, figsize=(8, 5)) # Creates a four histogram plot, number of rows and columns specified and the size of the figure in inches
setosa["sepal_length"].hist(ax=axes1[0], color= "darkgreen", alpha=0.8) #axes1[0]= the first histogram of the row in column one
axes1[0].set_title("Setosa Sepal Length")

versicolor["sepal_length"].hist(ax=axes1[1], color= "darkgreen", alpha=0.75)
axes1[1].set_title("Versicolor Sepal Length")

virginica["sepal_length"].hist(ax=axes1[2], color= "darkgreen", alpha=0.7)
axes1[2].set_title("Virginica Sepal Length")
#plt.savefig("sepal_length_comparison.png")
#plt.show()

fig2, axes2= plt.subplots(nrows=1, ncols=3, figsize=(8,5))
setosa["sepal_width"].hist(ax=axes2[0], color= "darkgreen", alpha=0.8)
axes2[0].set_title("Setosa Sepal Width")

versicolor["sepal_width"].hist(ax=axes2[1], color= "darkgreen", alpha=0.75)
axes2[1].set_title("Versicolor Sepal Width")

virginica["sepal_width"].hist(ax=axes2[2], color= "darkgreen", alpha=0.7)
axes2[2].set_title("Virginica Sepal Width")
#plt.savefig("sepal_width_comparison.png")
#plt.show()

fig3, axes3= plt.subplots(nrows=1, ncols=3, figsize=(8,5))
setosa["petal_length"].hist(ax=axes3[0], color="#5E47CB", alpha=0.8)
axes3[0].set_title("Setosa Petal Length")

versicolor["petal_length"].hist(ax=axes3[1], color="#5E47CB", alpha=0.75)
axes3[1].set_title("Versicolor Petal Length")

virginica["petal_length"].hist(ax=axes3[2], color="#5E47CB", alpha=0.7)
axes3[2].set_title("Virginica Petal Length")
#plt.savefig("petal_length_comparison.png")
#plt.show()

fig4, axes4= plt.subplots(nrows=1, ncols=3, figsize=(8,5))
setosa["petal_width"].hist(ax=axes4[0], color="#5E47CB", alpha=0.8)
axes4[0].set_title("Setosa Petal Width")

versicolor["petal_width"].hist(ax=axes4[1], color="#5E47CB", alpha=0.75)
axes4[1].set_title("Versicolor Petal Width")

virginica["petal_width"].hist(ax=axes4[2], color="#5E47CB", alpha=0.7)
axes4[2].set_title("Virginica Petal Width")
#plt.savefig("petal_width_comparison.png")
#plt.show()

# Overlapping histograms petal length and sepals