# create a list named my_list with 4 elements: a float, an integer, a string and another list
my_list = [2.5, 5, 'Hey', ['a', 10]]

# x is the 2nd element of my_list

x = my_list[1]
# y is the second element of the list which is the 4th element of my_list

y = my_list[-1][1]

# list slicing that returns a new list called z with the first 2 elements of my_list

z = list()
z.extend(my_list[:2])
print(z)