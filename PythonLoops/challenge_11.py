# Write a Python script that prints out the Fibonacci series up to a given number n.


n = int(input('Fibonacci series until:'))
value1, value2 = 0, 1
while value1 <= n:
    print(value1, ' ', end=' ')
    value1, value2 = value2, value1 + value2
