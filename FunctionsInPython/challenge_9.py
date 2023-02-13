# Define a function that draws a Christmas tree using asterisks (*). The function takes a single argument,
# which is the height of the tree.
def christmas_tree(x):
    for i in list(range(0, x + 1)):
        print('*' * i)


christmas_tree(10)
