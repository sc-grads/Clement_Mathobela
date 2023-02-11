# Write a Python script that displays the following pattern from 1 to n
# where n is entered by the user.

n = int(input('Enter a number:')) + 1
numbers = list(range(n))

for i in numbers:
    x = str(i) * i
    print(x)
