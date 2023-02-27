# Write a Python script that converts foot [ft] to centimeter [cm]. 1 ft = 30.48 cm

# The user will be prompted to enter the value in ft.

# Display the value in cm with 2 decimals, formatted using an f-string.

foot = input("Enter a measurement in foot so I can convert it to centimeters:")

print(f'The measurement in centimeter is {float(foot) * 30.48:.2f}')

