
#Considering the following dict, get a dict representation sorted by value.

d1 = {'x': 5, 'a': 3, 'c': 2, 'b': 0}

#A dict representation means viewing or printing the dict.
dict_view = sorted(d1.items(), key = lambda x: x[1])
print(dict_view)