# This programme will:
# Output a summary of each variable to a single text file,  
# Save a histogram of each variable to png files, and  
# Output a scatter plot of each pair of variables.  
# Author: Joanna Kelly

import pandas as pd

iris = pd.read_csv("iris.csv")
df = pd.DataFrame(iris)

description = df.describe()
print(description)

