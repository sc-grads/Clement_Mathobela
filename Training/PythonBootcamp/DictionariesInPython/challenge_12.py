# Consider the following 2 Lists:
names = ["Dan", "John", "Diana"]
phones = [11111, 2222, 3333]
# Create a set that contains the elements of the 2 lists in pairs.
# The resulting set should be: {('John', 2222), ('Diana', 3333), ('Dan', 11111)}
my_set = zip(names,phones)
print(set(my_set))
