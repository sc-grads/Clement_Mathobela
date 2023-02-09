# Write a Python script that prompts the user for the radius of a circle
# and calculates its area. Circle's area = pi * r ** 2 where pi = 3.1415
# Using an f-string display the area of the circle with 4 decimal places.

radius = float(input("Enter a circle's radius and i will tell you its area:"))

PI = 3.1415

print(f'the area of the circle is {PI * radius ** 2:.4f}')
