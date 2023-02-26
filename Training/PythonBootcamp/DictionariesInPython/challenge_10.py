# Consider the following two Python Lists that save information about company sales for the last 6 years:
years = [2015, 2016, 2017, 2018, 2019, 2020]
sales = [350000, 400000, 410000, 439000, 500000, 290000]
# Create a new dictionary that has the keys, the years, and the values, the sales.
# The resulting dict should be: {2015: 350000, 2016: 400000, 2017: 410000, 2018: 439000, 2019: 500000, 2020: 290000}
my_dict = dict(zip(years, sales))
print(my_dict)
