import csv
with open('people2.csv', 'w') as csvfile:
  writer = csv.writer(csvfile, delimiter = ':')
  people = [['Dan', 34, 'Bucharest'],['Andrei',21, 'London'],['Maria', 45, 'Paris']]
  for i in people:
    writer.writerow(i)

with open('people1.csv', 'r') as csvfile:
  reader = csv.reader(csvfile, delimiter = ":")
  for i in reader:
    print(i)