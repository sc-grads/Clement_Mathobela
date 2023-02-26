# Consider the following two Python Lists that save information about company sales for the last 6 years:
years = [2015, 2016, 2017, 2018, 2019, 2020]
sales = [350000, 400000, 410000, 439000, 500000, 290000]
# Create a new list that connects the year to the corresponding sales.
# The resulting list should be: [(2015, 350000), (2016, 400000),
# (2017, 410000), (2018, 439000), (2019, 500000), (2020, 290000)]
my_list = list(zip(years, sales))
print(my_list)