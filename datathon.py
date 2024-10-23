# -- coding: utf-8 --

import pandas as pd
from scipy.io import savemat

import os

current_path = os.getcwd()
print(current_path)

import numpy as np


# Synthetic data generation
# Define the dimensions of the 2D array
nHomes = 10
nAttributes = 3

# Define the lower and upper bounds for each column
# randomly generating [بعد السكن عن مكان العمل, عدد الغرف ،سعر الوحدة]
lower_bounds = [100000 , -1,      0] #عدد الغرف بالسالب بسبب أن كثرة الغرف أفضل
upper_bounds = [1000000, -5, 100000]

# Generate the 2D array with different bounds for each column
homesData = np.array([np.random.uniform(low=lower_bounds[i], high=upper_bounds[i], size=nHomes) for i in range(nAttributes)]).T

# print(homesData)
# Python 3 program to demonstrate working
# of method 1 and method 2.
# rows, cols = (nHomes, nHomes)

# method 2 1st approach
competitionMatrix=[]
rows, cols = nHomes, nHomes
for i in range(rows):
    col = []
    for j in range(cols):
        col.append(0)
    competitionMatrix.append(col)
#print(competitionMatrix)

for iHome in range(nHomes):
  for jHome in range(nHomes):
    if iHome == jHome:
      competitionMatrix[iHome][jHome] = 0.5
    else:
      temp = 0.0
      for iAttribute in range(nAttributes):
        if homesData[iHome,iAttribute] == homesData[jHome,iAttribute]:
          temp = temp + 0.5
        else:
          temp = temp + (int)(homesData[iHome,iAttribute] < homesData[jHome,iAttribute])
      temp = temp/nAttributes
      competitionMatrix[iHome][jHome] = temp

total_win_scores = [sum(row) for row in competitionMatrix]

# Sorting to find the winner home
# Sorting the list and returning the indices
sorted_with_indices = sorted(enumerate(total_win_scores), key=lambda x: x[1], reverse=True)

# Extracting the sorted list and indices
sorted_list = [item[1] for item in sorted_with_indices]
sorted_indices = [item[0] for item in sorted_with_indices]

print("Sorted List:", sorted_list)
print("Sorted Indices:", sorted_indices)

print('The Home with index zero is the most suitable for the user')
