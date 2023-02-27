import json
import requests
import csv

response = requests.get("https://jsonplaceholder.typicode.com/users")
users = json.loads(response.text)

# opening the csv file for writing
with open('users.csv', 'w') as f:
    writer = csv.writer(f)

    # write a header to file
    writer.writerow(("Name", "City", "GPS", "Company"))

    # iterating over the users list
    for user in users:
        # getting the data from the dictionary
        name = user['name']
        city = user['address']['city']
        lat = user['address']['geo']['lat']
        lng = user['address']['geo']['lng']
        # constructing the GPS coordinates in form of (lat, lng)
        geo = f'({lat},{lng})'
        company_name = user['company']['name']

        # writing to csv file
        csv_data = (name, city, geo, company_name)
        writer.writerow(csv_data)