#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 16:39:20 2020

@author: stephen
"""
import pandas as pd
import numpy as np
import os
# =============================================================================
# [1] Reading in a CSV file
# =============================================================================

# [i] Download and save the .csv file located in this weeks github folder.
# Done with git pull. Change directory to path of the file.
os.chdir("/home/josemari/CRTWorkshop/Data-Science-For-Life-Science/Introduction_to_Python/part_2")
# [ii] Open the csv file using pandas and save it to a variable.
days_df = pd.DataFrame(pd.read_csv("example_csv.csv", index_col = 0))
print(days_df)
# =============================================================================
# [2] Data exploration
# =============================================================================

# [i] Explore the top and bottom of the data.
print(days_df.head())
print(days_df.tail())

# [ii] How many rows and columns does the data have?
print(days_df.shape)

# [iii] Get the transpose of thise dataframe. Would it be better to use this?
days_trans = days_df.T
print(days_trans)

# [iv] Get the summary statistics of the data and save it to a variable.
days_stats = days_df.describe()
print(days_stats)

# [v] Using what you know about indexing Dataframes pull out the value of the
#     standard deviation for Wed from the variable you created in [2][iii].
std_wed = days_stats.loc["std"]["Wed"]
print(std_wed)

# =============================================================================
# [3] Indexing dataframes
# =============================================================================

# [i] Select the information for the 'Tue' column only and assign it to a variable.
tue = days_df["Tue"]
print(tue)

# [ii] Select rows 20 to rows 50.
print(days_df[20:50])

# [iii] Select only the weekday columns.
print(days_df.loc[:, "Mon":"Fri"])
# or
print(days_df[days_df.columns[0:5]])

# =============================================================================
# [4] Dropping and adding information
# =============================================================================

# [i] Drop the weekend columns and drop any row of your choice.
#     Use inplace to remove it from the original data, otherwise it will only
#     show the output on the console.
# Remove columns with indices 5 and 6.
days_df.drop(days_df.iloc[:, 5:7], axis = 1, inplace = True)
# Remove row 4
days_df.drop(4, axis = 0, inplace = True)
print(days_df)

# [ii] Change all NAs in the dataframe to 0.
days_df.fillna(value = 0, inplace = True)
print(days_df)

# [iii] Filter the dataframe so that it only contains the rows where the 'Mon'
#       column is greater than 50 (it will still contain all columns).
# Get the Monday values that are greater than 50 and store it in a variable.
mon_greater_50 = days_df[days_df["Mon"] > 50]
# Get all rows matching the conditions with the specified columns.
mon_greater_50.loc[:, "Mon":"Fri"]
# Do it all in one stage. First specied the condition to filter the dataframe,
# then get all rows that match it with the specified columns.
days_df[days_df["Mon"] > 50].loc[:, "Mon":"Fri"]

# [iv] Create a new column that is Mon column multiplied by 10.
new_column = days_df["Mon"] * 10
# Add the new column to the dataset with same indices as the dataset.
days_df["Mon x 10"] = pd.Series(new_column, index = days_df.index)
print(days_df)

# [v] Create a new row with any 6 values and add it to your dataframe.
from numpy.random import randint
# Create a new dataframe with row values, the column names matching the
# dataset columns and append it to the dataset.
new_row = pd.DataFrame([randint(low = 0, high = 100, size = 6)], columns = days_df.columns)
days_df = days_df.append(new_row)
print(days_df)

# =============================================================================
# [] Outputting a file
# =============================================================================

# [i] Output your modified cvs file to your working directory
days_df.to_csv("Modified_days.csv")

