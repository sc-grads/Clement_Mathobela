#################################
## Plotly - Creating Line Charts
#################################

## Importing the required modules
## We use the plotly.offline module if we generate out charts locally. Plotly company also offers an
## online service for creating charts.

import plotly.offline as pyo
import plotly.graph_objs as go
import random

pyo.init_notebook_mode()  ## for plotting inside Jupyter Notebook

x_values = list(range(50))
y_values = [random.randrange(20, 25) for x in range(50)]  # 50 random values between 20 and 24

## In Plotly, the Scatter function is used for scatter plots, line plots and bubble charts.
## Each trace is a line chart we put on the figure
trace1 = go.Scatter(x=x_values, y=y_values, mode='lines', name='Just Lines')

y_values = [random.randrange(15, 20) for x in range(50)]  # 50 random values between 15 and 19
trace2 = go.Scatter(x=x_values, y=y_values, mode='markers', name='Just Markers')

y_values = [random.randrange(10, 15) for x in range(50)]  # 50 random values between 10 and 14
trace3 = go.Scatter(x=x_values, y=y_values, mode='lines+markers', name='Markers and Lines')

data = [trace1, trace2, trace3]

## set the layout of the figure
## title on top of the plot
## the name of the x and y axis (both are valid ways of creating dictionaries,
## in plotly documentation we'll see the 2nd way)
layout = go.Layout(title='Simple Line Chart',
                   xaxis={'title': 'This is the X Axis'},
                   yaxis=dict(title='This is the Y Asis')
                   )

fig = go.Figure(data=data, layout=layout)

pyo.iplot(fig)  ## plot inside Jupyter Notebook
# OR:
## Generating a new html file
# pyo.plot(fig, filename='scatter_plot.html')


## Line Chart - Gold Annual Price
import pandas as pd

df = pd.read_csv('gold_annual_price.csv')  # csv file attached to the lecture

trace = go.Scatter(x=df.Date, y=df.Price, mode='lines', name='Gold Price')

data = [trace]
layout = go.Layout(title='Gold Monthly Price (1950-2019)')
fig = go.Figure(data=data, layout=layout)

pyo.iplot(fig)  ## plot inside Jupyter Notebook
# OR:
## Generating a new html file
# pyo.plot(fig, filename='scatter_plot.html')