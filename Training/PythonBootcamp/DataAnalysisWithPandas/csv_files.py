#################################
## Pandas - Reading CSV Files
#################################


import pandas as pd

df = pd.read_csv('countries_of_the_world.csv',
                 delimiter=',')  # The countries_of_the_world.csv is attached to this lecture

## A concise summary of this data frame
df.info()

## Setting display options
pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 50)
pd.set_option('display.width', 1000)

df.head()  # => first 5 rows
df.head(10)  # => first 10 rows

## Some filtering
df[df['Population'] > 100_000_000][['Country', 'Population', 'Area (sq. mi.)']]

## Sorting data
df[df['Population'] > 100_000_000][['Country', 'Population', 'Area (sq. mi.)']].sort_values('Population',
                                                                                            ascending=False)

x = df['GDP ($ per capita)'].idxmax()
df.iloc[x]

## Select all countries in either Estearn Europe or Western Europe and sorting by population in descending order.
region = df['Region'].str.strip().isin(['EASTERN EUROPE', 'WESTERN EUROPE'])  # this is a boolean series
df[region].sort_values('Population', ascending=False)

## The n largest countries by Population
df.nlargest(3, 'Population')

df.nlargest(5, 'GDP ($ per capita)')

df.nlargest(n=2, columns='Birthrate')

## The n smallest countries by Area
df.nsmallest(5, 'Area (sq. mi.)')