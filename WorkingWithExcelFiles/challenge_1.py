#Create a Python script that uses openpyxl and generates an Excel file with a single sheet and the below content:
import openpyxl
wb = openpyxl.Workbook()
sheet = wb.active
sheet['A1'] = 'Year'
sheet['B1'] = 'Sales'

my_dict = {2017:150_000, 2018:180_000, 2019:210_000, 2020:125_000}

for k,v in my_dict.items():
  sheet.append((k,v))
wb.save('sales.xlsx')