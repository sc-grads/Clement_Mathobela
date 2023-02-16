# Create a Python script that contains a function called excel2csv() which exports any Excel file to CSV one.

def excel2csv(xl_file, csv_file):
    import openpyxl
    import csv

    wb = openpyxl.load_workbook(xl_file)
    sheet = wb.active
    with open(csv_file, 'w') as file:
        writer = csv.writer(file)
        for row in sheet.values:
            writer.writerow(row)


excel2csv('books.xlsx', 'booklist.csv')