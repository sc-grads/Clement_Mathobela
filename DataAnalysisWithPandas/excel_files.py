#################################
## Pandas - Reading HTML Files
#################################

import pandas as pd
import xlrd  # this module should be installed

df = pd.read_excel('salaries.xlsx', sheet_name='Sheet1')  ## You find salaries.xlsx attached to the lecture

## Some statistics

df['Salary'].mean()  # => 54230.769230769234
df['Salary'].max()  # => 81000
df['Salary'].min()  # => 32000
df['Salary'].count()  # => 13
df['Salary'].std()  # => 14827.64223870317

## Returning unique values in a column
df['Country'].unique()  # => array(['USA', 'Brazil', 'Germany', 'UK'], dtype=object)

## Number of unique values
df['Country'].nunique()  # => df['Country'].value_counts()

df['Country'].value_counts()

df.sort_values('Salary', ascending=False)

##  Grouping together rows based on a column and then performing aggregate functions on them
c = df.groupby('Country')

c.max()  # it returns the maximum salary of all employees from each country
#  Name   Salary
# Country
# Brazil   Elizabeth  62000
# Germany  Eduard 81000
# UK   Oliver 71000
# USA  Marry  72000

c.min()
c.sum()  # it returns the sum of salaries of all employees from each country
c.mean()  # it returns the mean salary value for each country
c.std()  # it returns the standard deviation of salaries for each country

## The result of these pandas aggregate funtions is another pandas data frame
df1 = c.max()
df1.loc['UK']
# Name      Oliver
# Salary     71000
# Name: UK, dtype: object


df.groupby('Country').min().loc['USA']
# Name      Diana
# Salary    40000
# Name: USA, dtype: object


df.groupby('Country').describe()
#  Salary
# count    mean   std    min    25%    50%    75%    max
# Country
# Brazil   3.0    47333.333333   15011.106999   32000.0    40000.0    48000.0    55000.0    62000.0
# Germany  3.0    53666.666667   24193.663082   35000.0    40000.0    45000.0    63000.0    81000.0
# UK   3.0    60333.333333   11015.141095   49000.0    55000.0    61000.0    66000.0    71000.0
# USA  4.0    55250.000000   13098.982149   40000.0    50500.0    54500.0    59250.0    72000.0


df.groupby('Country').describe().transpose()