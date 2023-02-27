#################################
## Working with Excel Files in Python
## The OpenPyXL Module
## Creating a new Excel File
#################################

## Importing the module
import openpyxl

## Creating an in-memory Workbook
wb = openpyxl.Workbook()

## Getting the active sheet. This will be the only sheet in the workbook
sheet = wb.active

## Updating the new sheet using cells' addresses
sheet['A1'] = 'Year'
sheet['B1'] = 'Sales'

sales = {2017: 700000, 2018: 800000, 2019: 900000}  # dictionary

## Iterating over the dictionary and appending to the sheet
for k, v in sales.items():
    sheet.append((k, v))

## Saving the Workbook (in the same directory with the python script)
wb.save('sales.xlsx')