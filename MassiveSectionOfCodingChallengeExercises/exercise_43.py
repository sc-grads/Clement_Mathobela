# List with duplicates
years = [2010, 2010, 2011, 2011, 2012, 2012, 2012]

# New list with unique elements
years_unique = []

# YOUR CODE STARTS HERE
[years_unique.append(i) for i in years if i not in years_unique]
print(years_unique)