name = input("Enter your name")  # prompt user for their name
weight = input("Enter your weight in kilograms(kg)")  # prompt user for their weight
height = input("Enter your height in meters")  # prompt user for their height

BMI = float(weight) / (float(height)**2)  # Body mass index formula

print("Hi,", name, "your Body mass index is:", BMI)
