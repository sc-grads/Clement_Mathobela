# Create a Python script that removes all the elements of a list that are duplicates.
# Do the challenge in a single line of code using sets.

my_list = ['a', 'b', 1, 5, 1, 'a', 'z']

no_duplicate = list(set(my_list))
print(no_duplicate)
