#Create a function that takes an integer as an argument and returns True if it’s a prime number and False otherwise.
def my_prime(n):
    prime = True
    if n == 1:
        return False
    i = 1
    while i < n // 2:
        i = i + 1
        if n % i == 0:
            prime = False
            break
    return prime
print(my_prime(2))