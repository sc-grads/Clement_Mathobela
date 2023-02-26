#################################
## Plotly - Creating Histograms
#################################

## Importing the required modules
## We use the plotly.offline module if we generate out charts locally. Plotly company also offers an
## online service for creating charts.
import plotly.offline as pyo
import plotly.graph_objs as go
import random

pyo.init_notebook_mode()  ## for plotting inside Jupyter Notebook

## a list with 100 random values between 1 and 99
x_values = [random.randint(1, 100) for n in range(100)]

data = [go.Histogram(x=x_values)]
layout = go.Layout(title='Simple Histogram')
fig = go.Figure(data, layout)

pyo.iplot(fig)  ## plot inside Jupyter Notebook
## Generating a new html file
# pyo.plot(fig, filename='scatter_plot.html')

## Histogram of Monthly Salary
import pandas as pd

df = pd.read_csv('monthly_salary.csv')  # the csv file is attached to the lecture
x_values = df['Monthly Salary']

# data = [go.Histogram(x=x_values)]
## Using a bin size of 100, starting and ending values
data = [go.Histogram(x=x_values, xbins=dict(start=3000, end=5000, size=100))]

layout = go.Layout(title='Histogram of Monthly Salary')
fig = go.Figure(data, layout)
pyo.iplot(fig)