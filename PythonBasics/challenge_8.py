#  the comparison operator returns False instead of True.
#  Your job is to modify the code so that the comparison returns True which is correct.

from math import isclose

a = 0.1
b = 0.3

# print(a * 3 == b)
print(isclose(a * 3, b, rel_tol=0.02))
