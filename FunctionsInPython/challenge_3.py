# Write a function that returns the factorial of a number n which is the function's argument.
def factorial(number):
    if number == 0:
        return 1
    else:
        f = 1
        while number > 0:
            f *= number
            number -= 1
    return f


print(factorial(5))
