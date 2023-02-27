# Write a Python function that takes a list as an argument
# and returns a new list with unique elements of the first list in the same order.
# Sample List : [1,2,3,3,3,3,4,5, 1, 3, 5, 5, 5]
# Unique List : [1, 2, 3, 4, 5]
my_list = [1, 2, 3, 3, 3, 3, 4, 5, 1, 3, 5, 5, 5]
my_unique_list = sorted(list(set(my_list)))
print(my_unique_list)
