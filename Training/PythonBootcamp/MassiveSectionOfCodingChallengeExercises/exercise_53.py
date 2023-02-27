countries = {'us': 'United States of America', 'br': 'Brazil', 'de': 'Germany', 'at': 'Austria'}

# YOUR CODE STARTS HERE
# print out the values of the dictionary sorted by keys alphabetically. Each value should be on its own line.

keys = sorted(countries.keys())

for k in keys:
    print(countries[k])
