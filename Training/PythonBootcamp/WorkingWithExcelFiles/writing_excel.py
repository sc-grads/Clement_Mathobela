#################################
## Working with Excel Files in Python
## The OpenPyXL Module
## Writing Excel Files
#################################

## Importing the module
import openpyxl

## Loading an excel file. store.xlsx is in the same directory with the python script
wb = openpyxl.load_workbook('store.xlsx')

## Getting the active sheet (last opened sheet)
sheet = wb.active

## Change the value in cell
sheet['d2'] = 400

## Adding a new row
new_product = (11, 'Tablet', 12, 600, 12 * 600)  # this is a tuple
sheet.append(new_product)

## Iterating and updating an entire column
for c, d, e in sheet['c2:e12']:
    e.value = c.value * d.value

## Saving the file
wb.save('store.xlsx')