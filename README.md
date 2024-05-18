# Fisher Iris Dataset

## Introduction

The data set I analysed was the Fisher Iris data set. I used the data set to create histograms and scatter plots in order to gain insights into the characteristics of different iris species. 

The Fisher Iris data set centres around three species; Setosa, Versicolor and Virginica, from which 50 samples were taken each. Four measurements were taken from two places, the sepal (length and width) and the petals (length and width). 

At the time of the dataset being created, statistician and biologist, Ronald Fisher used the data to develop a way to differentiate the species by their characteristics, creating a linear discriminant analysis.

Sepals are characterised as laying flat and are the "landing pads" for bees and other insects, whilst the petals stand straight upwards. 
![Iris flower with sepal and petal labels]("C:\Users\joann\Downloads\Iris Flower Labelled.jpg")

Repository
The repository contains four files and a directory:
README.md:
Background and overview
A breakdown of the process of creating the script for analysis.py
Instructions for using the code 
References

analysis.py
Contains the script used to analyse the data.

iris.csv
Is the source of the dataset used.

summary_statistics.txt
Contains the mean, standard deviation and the minimum and maximum values of each variable in the data set.

My-plots
Is the directory containing all plots generated using analysis.py.


Analysis.py
To run the code, the user will need to have Python available to use on their computer, which can be downloaded from the official website (). The raw script (analysis.py) can be cloned and downloaded from Github. Afterwards, the user will need to open a terminal and navigate to the directory that contains the raw code. From there the user can run the code by typing in the following command: python analysis.py. 

Firstly to begin writing my Python code, I had to download the Fisher Iris dataset and save it as a csv file within my repository to use the data for analysis (). Secondly I had to import all relevant libraries as follows: pandas, os and matplotlib.py. Then I could create my variables, for example “iris”, “setosa”, “versicolor” and “virginica”. With the variable “iris”, I could create a subplot of histograms to give an overview of each variable (sepal length and width, and petal length and width). Subplots of histograms to compare sepal length, sepal width, petal length and petal width between the three species are also created. Two scatter plots are created to show the correlation between each pair of variables, however all species are included. And finally I created a directory in order to store the plots. 

References
Where I download the iris dataset:
https://gist.github.com/curran/a08a1080b88344b0c8a7

Python download:
https://www.python.org/downloads/release/python-3123/

Matplotlib from CSV file: 
https://www.tutorialspoint.com/plot-data-from-csv-file-with-matplotlib

How to create the various plots (histogram and scatter plots):
https://pandas.pydata.org/docs/getting_started/intro_tutorials/04_plotting.html

Save a histogram to a png file:
https://www.tutorialspoint.com/how-to-save-a-histogram-plot-in-python

Overlapping problem:
https://matplotlib.org/stable/users/explain/axes/tight_layout_guide.html

Scatter plot colour problem:
https://stackoverflow.com/questions/12236566/setting-different-color-for-each-series-in-scatter-plot

Improving code readability:
https://realpython.com/python-pep8/#:~:text=PEP%208%2C%20sometimes%20spelled%20PEP8,and%20consistency%20of%20Python%20code.

Import os:
https://docs.python.org/3/library/os.html
https://www.geeksforgeeks.org/os-module-python-examples/

How to use markdown (cheat sheet and basic syntax):
https://www.markdownguide.org/basic-syntax/

Public domain iris images:
https://www.backyardnature.net/
https://www.fs.usda.gov/wildflowers/beauty/iris/flower.shtml