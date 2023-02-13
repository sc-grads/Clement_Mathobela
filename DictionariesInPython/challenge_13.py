# Consider the two Python lists. Write a Python Script to make a new list whose elements are the intersection of #
# the two given lists. This means all elements of L1 that also belong to L2, but no other elements.
my_list1 = [1, 2, 3, 'a', 'b', 'z']
my_list2 = [1, 'x', 'p', 2, 'z']
my_list3 = list(set(my_list1).intersection(set(my_list2)))
print(my_list3)
