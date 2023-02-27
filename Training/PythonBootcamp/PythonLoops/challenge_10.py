# Write a Python program that iterates over the integers from 1 to 50.

# For multiples of three print "Foo" instead of the number and for multiples of five print "Bar".

# For numbers that are multiples of both three and five print "FooBar".

for i in range(1, 51):

    if (i % 3) == 0 and (i % 5) == 0:
        print(F'{i}:FooBar')
    elif (i % 3) == 0:
        print(F'{i}:Foo')

    elif (i % 5) == 0:
        print(F'{i}:Bar')