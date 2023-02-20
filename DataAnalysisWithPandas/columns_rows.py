#################################
## Pandas DataFrames I
## A Data Frame is a two - dimensional size, mutable and potentially heterogeneous tabular data structure
## with labeled axes (rows and columns).This can be thought of as a dictionary-like container for Series objects.
## A data frame is the primary Pandas data structure.
#################################

import pandas as pd

data = [['Dan', 30, 40000], ['John', 40, 50000],
        ['Helen', 35, 60000], ['Marry', 29, 58000]]

## Creting a Pandas DataFrame
## No. of columns must match the no. of columns or it returns error
df = pd.DataFrame(data, columns=['Name', 'Age', 'Salary'])
print(df)
#  Name   Age    Salary
# 0    Dan    30 40000
# 1    John   40 50000
# 2    Helen  35 60000
# 3    Marry  29 58000

type(df), type(df['Name'])  # => (pandas.core.frame.DataFrame, pandas.core.series.Series)

## Returning the no. of rows and columns in the dataframe
print(df.shape)  # => (4, 3)

## Returning a column
## We access a values in a column like a value of dictionary key
df['Name']
df.Name  ## Alternative syntax
# 0      Dan
# 1     John
# 2    Helen
# 3    Marry
# Name: Name, dtype: object

## Returning more columns
df[['Name', 'Salary']]
# Name Salary
# 0    Dan    40000
# 1    John   50000
# 2    Helen  60000
# 3    Marry  58000

## Adding a new column
df['Phone'] = ['11111', '22222', '33333', '44444']

## Dropping Rows and Columns
# Dropping row at index 2. The second argument is axis. 0 means rows and 1 means columns
df.drop(2, 0)

## Dropping column 'Age'
## It doesn't modify the data frame, just returns a new modified data frame
df.drop('Age', axis=1)

## Dropping column 'Age' in-place (modifies the dataframe)
df.drop('Age', axis=1, inplace=True)

## Renaming Columns
df.rename(columns={'Name': 'First Name', 'Salary': 'Annual Salary'}, inplace=True)

### Selecting Rows
data = [['Dan', 30, 40000], ['John', 40, 50000],
        ['Helen', 35, 60000], ['Marry', 29, 58000]]
df = pd.DataFrame(data, columns=['Name', 'Age', 'Salary'])
#  Name   Age    Salary
# 0    Dan    30 40000
# 1    John   40 50000
# 2    Helen  35 60000
# 3    Marry  29 58000

# Returning the entry at index 0
df.loc[0]
# Name        Dan
# Age          30
# Salary    40000
# Name: 0, dtype: object

## The first argument is the label or the index of the row and the second is the column name
df.loc[1, 'Name']  # => 'John'
type(df.loc[0])  # => pandas.core.series.Series

## Reading and Returning rows between index 0 and 2 included
df.loc[0:2]

# Returning entries at index 0, 1, 2, 3 and only some columns. Take care at the syntax!!!
df.loc[[0, 1, 3], ['Name', 'Annual Salary']]
df.loc[0:2, ['Name', 'Mobile Phone']]

## Returning all rows but only some columns
df.loc[:, ['Name', 'Annual Salary']]

## Returns the row at position 0 (even if the data frame is indexed by strings ar something else, not numbers)
## Indexes start from zero
df.iloc[0]
# Name        Dan
# Age          30
# Salary    40000
# Name: 0, dtype: object


df.iloc[0, 1]  # returns the value at index 0 (row 0) and column at index 1 which is the age

df.iloc[0:3]  # from zero to three excluded, all columns

df.iloc[3, 0:2]  # row at index 3, columns 0-2

df.iloc[[1, 3], 0:2]  # rows 1-3 excluded, column 0-2 excluded

## Returning a random row
df.sample()

## Returning 2 random rows
df.sample(n=2)

# Returning a random 20% fraction
df.sample(frac=0.2)

## Creating a Python Dictionary from 2 DataFrame columns
dict(zip(df['Name'], df['Age']))