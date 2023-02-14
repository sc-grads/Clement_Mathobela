# Write a Python function to check whether a number is perfect or not. The function should return True if the
# number is perfect and False otherwise

def my_divisors(n):
    divisors = []
    for x in range(1, int(n/2)+1):
        if n % x == 0:
            divisors.append(x)
    return divisors


def perfect_number(n):
    divs = my_divisors(n)
    if sum(divs) == n:
        return True
    else:
        return False


# calling the function
n = int(input('Enter a value:'))
if perfect_number(n):
    print('True')
else:
    print('False')
