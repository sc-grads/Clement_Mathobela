#################################
## Plotly - Creating Pie Charts
#################################

## Importing the required modules
## We use the plotly.offline module if we generate out charts locally. Plotly company also offers an
## online service for creating charts.

import plotly.offline as pyo
import plotly.graph_objs as go

pyo.init_notebook_mode()  ## for plotting inside Jupyter Notebook

labels = ['Nitrogen', 'Oxygen', 'Other']
values = [78.09, 20.95, 0.96]
my_colors = ['#0066cc', '#ffd700', '#dc0000']

data = [go.Pie(labels=labels, values=values, marker=dict(colors=my_colors))]

layout = go.Layout(title='Air Composition')
fig = go.Figure(data, layout)

pyo.iplot(fig)  ## plot inside Jupyter Notebook
## Generating a new html file
# pyo.plot(fig, filename='scatter_plot.html')


### Reading a HTML File using Pandas and creating a Pie Chart using Plotly

import pandas as pd

df = pd.read_html('https://en.wikipedia.org/wiki/List_of_continents_by_population')  ## list of DataFrames(tables)
type(df[0])  # => data frame
t1 = df[0]  # first table

## Using sclicing to skip the 1st row
labels = t1.loc[1:, 'Continent']
values = t1.loc[1:, '% of world pop.']

## Data frame processing
values[7] = values[7].lstrip('<')  ## strip < from the last row
values = values.str.rstrip('%').astype('float') / 100.0  ## strip % and convert to float between 0 and 1

data = [go.Pie(labels=labels, values=values)]

layout = go.Layout(title='World Population By Continent, 2016')
fig = go.Figure(data, layout)

pyo.iplot(fig)  ## plot inside Jupyter Notebook
## Generating a new html file
# pyo.plot(fig, filename='scatter_plot.html')