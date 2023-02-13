employees = {'John': ('London', 4000, 28), 'Maria': ('Zagreb', 3800, 40), 'Diana': ('NYC', 3500, 31)}
# Print a sorted view of the dictionary by the third field of its values, in reverse order.
my_dict = sorted(employees.items(), key=lambda x: x[1][2], reverse=True)
print(my_dict)