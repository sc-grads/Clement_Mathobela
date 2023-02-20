#################################
## Plotly - Creating Bar Charts
#################################

## Importing the required modules
## We use the plotly.offline module if we generate out charts locally. Plotly company also offers an
## online service for creating charts.

import plotly.offline as pyo
import plotly.graph_objs as go

pyo.init_notebook_mode()  ## for plotting inside Jupyter Notebook

## Creating Basic Bar Chart
x_axis = ['A', 'B', 'C', 'D']
y_axis = [10, 15, 23, 18]

data = [go.Bar(x=x_axis, y=y_axis)]
pyo.iplot(data)  ## plot inside Jupyter Notebook
## Generating a new html file
# pyo.plot(data, filename='scatter_plot.html')


## Reading the online CSV File with Pandas
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/school_earnings.csv")

data = [go.Bar(
    x=df.School,
    y=df.Gap,
    marker={'color': '#d50000'}  # change the default color
)]

pyo.iplot(data)  ## plot inside Jupyter Notebook
## Generating a new html file
# pyo.plot(data, filename='scatter_plot.html')


#################
## Grouped Bar Charts
################
## Birth and Deathrate of 10 random countries with a population greater than 100_000_000
full_df = pd.read_csv("countries_of_the_world.csv")  # the csv file is attached to the lecture

## Birth and Deathrate of 10 random countries with a population greater than 100_000_000
mask = full_df['Population'] > 100_000_000
df = full_df[mask].sort_values('Population', ascending=False)
df = df.sample(n=10)

# ## Birth and death rate of the first 10 largest countries in terms of population
# df = full_df.sort_values('Population', ascending=False)
# df = df.head(n=10)


trace1 = go.Bar(
    x=df['Country'],
    y=df['Birthrate'],
    name='Birthrate')

trace2 = go.Bar(
    x=df.Country,  # another way to access a column
    y=df.Deathrate,
    name='Deathrate')

data = [trace1, trace2]

layout = go.Layout(title='Birthrate/Deathrate of Random Country', barmode='group')
# layout = go.Layout(title='Birthrate/Deathrate of Random Country', barmode='stack')  ## stacked bar chart
fig = go.Figure(data=data, layout=layout)

pyo.iplot(fig)  ## plot inside Jupyter Notebook
## Generating a new html file
# pyo.plot(fig, filename='scatter_plot.html')