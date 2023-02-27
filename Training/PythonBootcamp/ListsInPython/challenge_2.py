# Create a Python script that removes all the elements of a list that are duplicates.
names = ['a', 'b', 'z', 'a', 'x', 1, 'w', 'z', 5, 3, 5, 1]
new_names = list()
for name in names:
    if name not in new_names:
        new_names.append(name)
print(new_names)
