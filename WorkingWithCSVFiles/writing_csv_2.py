import csv
with open('numbers.csv','w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['x', 'x**2', 'x**3'])
    for x in range(1, 16):
        writer.writerow([x, x**2, x**3])