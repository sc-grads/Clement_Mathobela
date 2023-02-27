#################################
## Pandas Series
## A series is a one dimensional labeled array and stores data. It has one dimension, so it stores one column of information.
## We can think of a series as of a basic pandas data type.
#################################

## Installing pandas
# pip install pandas  # => Windows/Mac
# pip3 install pandas # => Linux

## Importing pandas as pd
import pandas as pd

## Creating a Series
numbers = list(range(2, 11, 2))
s1 = pd.Series(numbers)
print(s1)
# 0     2
# 1     4
# 2     6
# 3     8
# 4    10
# dtype: int64

##dtype indicates the type of data that makes up the values of this series.

##  Indexes don't have to be numeric.
## They can be any data type and by default they are numeric values starting from zero.
labels = list('abcde')
print(labels)  # => ['a', 'b', 'c', 'd', 'e']

s2 = pd.Series(data=numbers, index=labels)
print(s2)

# a     2
# b     4
# c     6
# d     8
# e    10
# dtype: int64

## We can't create a Series from a set because set is unordered.
# pd.Series({1,2,3})    # => TypeError: 'set' type is unordered

## Creating a Series from a dictionary
my_dict = dict(zip(['a', 'b', 'c'], [1, 2, 3]))
my_dict = dict(zip(['a', 'b', 'c'], [1, 2, 3]))
print(my_dict)  # => {'a': 1, 'b': 2, 'c': 3}

s3 = pd.Series(my_dict)
print(s3)
# a    1
# b    2
# c    3
# dtype: int64

## Getting a value using the label
print(s3['a'])  # => 1