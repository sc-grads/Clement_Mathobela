# Create a Python script that asks the user for a number and then prints out a list of all the divisors of each number
# less than the asked number.


number = int(input("Enter a number: "))
divisors = list()
for i in range(2, number//2+1):
    if number % i == 0:
        divisors.append(i)

print(divisors)
