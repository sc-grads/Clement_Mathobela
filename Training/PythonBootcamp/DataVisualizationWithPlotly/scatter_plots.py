#################################
## Plotly - Creating Scatter Plots
#################################

## Importing the required modules
## We use the plotly.offline module if we generate out charts locally. Plotly company also offers an
## online service for creating charts.
import plotly.offline as pyo
import plotly.graph_objs as go

import random

## If you want to create the chart directly in jupyter notebook
## you have to call the init_notebook_mode() function of the python.offline module.
pyo.init_notebook_mode()

## Generating 50 random integer values between 0 and 19. These will be put on the x axis
x_values = [random.randrange(0, 20) for n in range(50)]
## 50 random values between -10 and 9 for the y axis
y_values = [random.randrange(-10, 10) for n in range(50)]

## In Plotly, the Scatter function of the graph_objs module is used to create scatter plots, line plots and bubble charts.
data = [go.Scatter(x=x_values, y=y_values, mode='markers')]

## Plot inside jupyter notebook
# pyo.iplot(data)
# OR:
## Generating a new html file
pyo.plot(data, filename='scatter_plot.html')

## Reading Data using Pandas
import pandas as pd

df = pd.read_csv('houses.csv')  ## houses.csv is attached to the scatter plots lecture

## both ways are correct
x_values = df['GroundLivingArea']
y_values = df.SalePrice

data = [go.Scatter(x=x_values, y=y_values, mode='markers')]
pyo.iplot(data)  ## plot inside Jupyter Notebook
# OR:
## Generating a new html file
# pyo.plot(data, filename='scatter_plot.html')