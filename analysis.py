# This programme will:
# Output a summary of each variable to a single text file,  
# Save a histogram of each variable to png files, and  
# Output a scatter plot of each pair of variables.  
# Author: Joanna Kelly

import pandas as pd    # imports pandas library and assigns the nickname 'pd'

iris = pd.read_csv("iris.csv") # Reads the data from a csv file and stores it in a pandas data frame

description = iris.describe() # This creates summary statistics for each variable
print(description)

