# Write a Python program to check if an integer (x) is the power of another integer (y).
# Prompt the user to input both integers.
# Input: 16, 2
# Output: 4 ** 2 = 16


x = int(input("Enter a number x: "))
y = int(input(f"Enter a number y: "))

found = False

for i in range(2, x // 2):
    if y ** i == x:
        print(f"{y} ** {i} = {x}")
        found = True
        break
else:
    print(f'{x} is not the power of {y}')
