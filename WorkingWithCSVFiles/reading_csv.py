import csv
with open('airtravel.csv') as file:
    content = csv.reader(file)
    next(content)
    my_dict = dict()
    for row in content:
        my_dict[row[0]] = row[2]

    max_1959 = max(my_dict.values())
    print(max_1959)
    for k,v in my_dict.items():
        if max_1959 == v:
            print(f'The busiest month in 1959 is {k} with {v.strip()} flight attendants')