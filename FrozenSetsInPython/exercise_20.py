set1 = {'a', 'b', 'c'}
set2 = {'c', 'd', 'e'}

# YOUR CODE STARTS HERE
# set3 contains all unique elements present in both set1 and set2
set3 = set1.union(set2)


# set4 contains the common elements of set1 and set2
set4 = set1.intersection(set2)

# set5 contains the elements that exist only in set1, but not in set2
set5 = set1.difference(set2)

# remove the element 'c' from set1
set1.remove('c')

