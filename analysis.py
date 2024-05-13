# This programme will:
# Output a summary of each variable to a single text file,  
# Save a histogram of each variable to png files, and  
# Output a scatter plot of each pair of variables.  
# Author: Joanna Kelly

# Importing necessary software:
import pandas as pd    # imports pandas library and assigns the nickname 'pd'
import os # software for creating directories and saving files to different directories    
import matplotlib.pyplot as plt # software to create my histograms and scatter plots

iris = pd.read_csv("iris.csv") # Reads the data from a csv file and stores it in a pandas data frame
description = iris.describe() # This creates summary statistics for each variable

with open("summary_statistics.txt", "w") as file:     # Creates a txt file 
    file.write(description.to_string())         # writes to the new file and converts the summary stats to a string

directory_name = "my_plots" # Name of directory
save_directory = os.path.join("\\Users\\joann\\Desktop\\pands\\pands-project", directory_name) # Need to use escape backslashes otherwise syntax error occurs
if not os.path.exists(save_directory):     # Checks to see if directory exists, creates the directory if not
    os.makedirs(save_directory)           # Creating a directory for plots to tidy up main project directory

# Creating a subplot of histograms for an overview of 4 variables:
variable_overview, axes= plt.subplots(nrows=2, ncols=2, figsize=(10, 6)) # Creates a four histogram plot, number of rows and columns specified and the size of the figure in inches
iris["sepal_length"].hist(ax=axes[0,0], color="darkgreen", alpha=0.7)  # isolates sepal length column and assigns it to row 1, column 1, alpha refers to the opacity
axes[0,0].set_xlabel("Length in cm") # labels the x axis, along the bottom
axes[0,0].set_ylabel("Frequency") # labels the y axis, up the side
axes[0,0].set_title("Sepal Length") # gives a title to this individual histogram

iris["sepal_width"].hist(ax=axes[0,1], color="darkgreen", alpha=0.7)
axes[0,1].set_xlabel("Width in cm")
axes[0,1].set_ylabel("Frequency")
axes[0,1].set_title("Sepal Width")

iris["petal_length"].hist(ax=axes[1,0], color="#5E47CB") # hexadecimal colour of random iris flower
axes[1,0].set_xlabel("Length in cm")
axes[1,0].set_ylabel("Frequency")
axes[1,0].set_title("Petal Length")

iris["petal_width"].hist(ax=axes[1,1], color="#5E47CB", alpha= 0.8)
axes[1,1].set_xlabel("Width in cm")
axes[1,1].set_ylabel("Frequency")
axes[1,1].set_title("Petal Width")
plt.tight_layout()  # prevents overlapping of subplots
plt.savefig(os.path.join(save_directory, "variable_overview_hist.png"))          # saves the histogram to a PNG file
#plt.show()  # displays the histogram when the program is run


#seperating the species:
setosa = iris[iris["species"]== "setosa"]  
versicolor = iris[iris["species"]== "versicolor"]
virginica = iris[iris["species"]== "virginica"]

# Creating a hist for the sepal lengths of each species
sepal_length_comp, axes1= plt.subplots(nrows=1, ncols=3, figsize=(8, 5)) # Creates a four histogram plot, number of rows and columns specified and the size of the figure in inches
setosa["sepal_length"].hist(ax=axes1[0], color= "darkgreen", alpha=0.8) #axes1[0]= the first histogram of the row in column one
axes1[0].set_title("Setosa Sepal Length")
axes1[0].set_xlabel("in cm")

versicolor["sepal_length"].hist(ax=axes1[1], color= "darkgreen", alpha=0.75)
axes1[1].set_title("Versicolor Sepal Length")
axes1[1].set_xlabel("in cm")

virginica["sepal_length"].hist(ax=axes1[2], color= "darkgreen", alpha=0.7)
axes1[2].set_title("Virginica Sepal Length")
axes1[2].set_xlabel("in cm")
plt.savefig(os.path.join(save_directory, "sepal_length_comparison.png"))


# Creating a hist for the sepal widths of each species
sepal_width_comp, axes2= plt.subplots(nrows=1, ncols=3, figsize=(8,5))
setosa["sepal_width"].hist(ax=axes2[0], color= "darkgreen", alpha=0.8)
axes2[0].set_title("Setosa Sepal Width")
axes2[0].set_xlabel("in cm")

versicolor["sepal_width"].hist(ax=axes2[1], color= "darkgreen", alpha=0.75)
axes2[1].set_title("Versicolor Sepal Width")
axes2[1].set_xlabel("in cm")

virginica["sepal_width"].hist(ax=axes2[2], color= "darkgreen", alpha=0.7)
axes2[2].set_title("Virginica Sepal Width")
axes2[2].set_xlabel("in cm")
plt.savefig(os.path.join(save_directory, "sepal_width_comparison.png"))


# Creating a hist for the petal lengths of each species
petal_length_comp, axes3= plt.subplots(nrows=1, ncols=3, figsize=(8,5))
setosa["petal_length"].hist(ax=axes3[0], color="#5E47CB", alpha=0.8)
axes3[0].set_title("Setosa Petal Length")
axes3[0].set_xlabel("in cm")

versicolor["petal_length"].hist(ax=axes3[1], color="#5E47CB", alpha=0.75)
axes3[1].set_title("Versicolor Petal Length")
axes3[1].set_xlabel("in cm")

virginica["petal_length"].hist(ax=axes3[2], color="#5E47CB", alpha=0.7)
axes3[2].set_title("Virginica Petal Length")
axes3[2].set_xlabel("in cm")
plt.savefig(os.path.join(save_directory, "petal_length_comparison.png"))


# Creating a hist for the petal widths of each species
petal_width_comp, axes4= plt.subplots(nrows=1, ncols=3, figsize=(8,5))
setosa["petal_width"].hist(ax=axes4[0], color="#5E47CB", alpha=0.8)
axes4[0].set_title("Setosa Petal Width")
axes4[0].set_xlabel("in cm")

versicolor["petal_width"].hist(ax=axes4[1], color="#5E47CB", alpha=0.75)
axes4[1].set_title("Versicolor Petal Width")
axes4[1].set_xlabel("in cm")

virginica["petal_width"].hist(ax=axes4[2], color="#5E47CB", alpha=0.7)
axes4[2].set_title("Virginica Petal Width")
axes4[2].set_xlabel("in cm")
plt.savefig(os.path.join(save_directory, "petal_width_comparison.png"))


#Creating a scatter plot with sepal lengths and sepal widths across all three species
iris.plot.scatter(x="sepal_length", y="sepal_width", color= "darkgreen", alpha=0.5) #plot.scatter creates our scatter plots
plt.title("Sepal Length and Width in cm")  #Creates a title
plt.savefig(os.path.join(save_directory, "sepal_scatter.png")) #saves the file

#Creating a scatter plot with petal lengths and petal widths across all three species
iris.plot.scatter(x="petal_length", y="petal_width", color="#5E47CB", alpha=0.5)
plt.title("Petal Length and Width in cm")
plt.savefig(os.path.join(save_directory, "petal_scatter.png"))