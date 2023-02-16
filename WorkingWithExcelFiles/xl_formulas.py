#################################
## Working with Excel Files in Python
## The OpenPyXL Module
## Using Excel Formulas
#################################

## Importing the module
import openpyxl

## Loading an excel file. store.xlsx is in the same directory with the python script
wb = openpyxl.load_workbook('store.xlsx')

## Getting a sheet by name
sheet = wb['Products']

## Iterating over a cell range and writing an Excel formula in each cell of a column
for c, d, e in sheet['c2:e12']:
    e.value = f'={c.coordinate}*{d.coordinate}'  # writing an Excel formula to each cell. The formula is written as a string

## Getting another sheet of the Workbook
sheet = wb['Sales 2018']

## Writing an Excel formula (=sum(B2:B13)
sheet['B14'] = '=sum(B2:B13)'

## Saving the file
wb.save('store.xlsx')