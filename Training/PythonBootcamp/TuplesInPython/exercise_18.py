languages = ('Python', 'Java', 'Go', 'C++', 'PHP', 'Scala', 'Solidity')

# Using a negative index extract the last element of the tuple in a variable called x
x = languages[-1]

# Return a new tuple called y using slicing and a step
# y should be ('Python', 'Scala')
y = tuple(languages[::5])