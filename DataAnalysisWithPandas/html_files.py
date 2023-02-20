#################################
## Pandas - Reading HTML Files
#################################

import pandas as pd

## dfs is a list of data frames. Each data frame is a html table
dfs = pd.read_html('https://en.wikipedia.org/wiki/List_of_European_cities_by_population_within_city_limits')

## Getting the first data frame (table)
df = dfs[0]
# print(df)


dfs = pd.read_html('https://www.nasdaq.com/symbol/amzn/historical')
df = dfs[2]
# print(df)

## Getting the maximum Opening Amazon Stock Price
i = df.iloc[:, 1].idxmax()
df.iloc[i]