#################################
## Working with Missing Data
## Within pandas, a missing value is denoted by NaN and is what most developers know as null.
#################################

import pandas as pd

## Creating a Pandas DataFrame form a Dictionary
my_dict = {'A': [1, 2, 3], 'B': [4, None, 6], 'C': [7, None, None]}
df = pd.DataFrame(my_dict)
print(df)
#    A    B    C
# 0  1  4.0  7.0
# 1  2  NaN  NaN
# 2  3  6.0  NaN

## Dropping all rows that have at least one NaN value
## It doesn't modify the data frame, it just returns a modified copy
df.dropna()

## Modifies the data frame in-place
df.dropna(inplace=True)

## Removing columns with one or more missing values
df.dropna(axis=1)

## Dropping only those rows or columns (axis=1) that have less than the threshold number of non-NaN values.
df.dropna(thresh=2)

## Filling missing values in our data frame.
df.fillna(value='PYTHON')

df['B'].fillna(value=100)

## Calculate the value it will fill using other Pandas functions.
df['B'].fillna(value=df['B'].mean())