# Write a Python program that displays the multiplication table
# (from 1 to 10) of a specific integer number entered by the user.

my_list = list(range(1, 11))
n = float(input('Enter a number to get a multiplication table:'))
for i in my_list:
    times = int(i * n)
    print(F'{n} multiply by {i} is {times}')