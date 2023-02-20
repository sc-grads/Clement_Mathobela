import requests
from bs4 import BeautifulSoup
import openpyxl

url = 'https://www.property24.com/apartments-to-rent/johannesburg/gauteng/100?sp=pt%3d10000#112320241'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

content = soup.find_all('div', class_='p24_content')
apartments = []

for item in content:

    price = item.div.div.text

    location = item.div.span.text
    apartments.append((price.strip(),location.strip()))
print(apartments)

wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = 'Rentals in Johannesburg'
sheet['A1'] = 'Price'
sheet['B1'] = 'Location'

for apartment in apartments:
    sheet.append(apartment)

wb.save('Apartments.xlsx')
