#Consider the Excel file generated in the previous challenge.
#Format the cells B6 and C6 in the following way: Tahoma font family, size 16, color red, and bold.


import openpyxl
from openpyxl.styles import *

wb = openpyxl.load_workbook('sales3.xlsx')

sheet = wb.active


font = Font(name='Tahoma', size=16, color=colors.RED, bold=True, italic=False, strike=False)
cell_b6 = sheet['B6']
cell_b6.font = font

cell_c6 = sheet['c6']
cell_c6.font = font


wb.save('sales3.xlsx')