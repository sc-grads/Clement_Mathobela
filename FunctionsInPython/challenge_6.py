#Write a function called fibo that takes an integer greater than 10 as an argument and returns the Fibonacci #series between 0 and the function's argument.

def fibo(n):
  a, b = 0, 1
  while a <= n:
    print(a, ' ', end=' ')
    a, b = b, a + b

fibo(25)