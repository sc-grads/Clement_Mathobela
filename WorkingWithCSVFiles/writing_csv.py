import csv
with open('people.csv', 'a') as file:
    writer = csv.writer(file)
    new_data = ('5', 'Clement', 'JHB')
    writer.writerow(new_data)
