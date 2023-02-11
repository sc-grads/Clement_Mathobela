# Write a Python program that calculates and displays the sum, the product and the average of n float numbers entered by the user, each on a separate line. Enter 0 to finish.
sum = 0
product = 1
count = 0

while True:
    value = float(input('Enter a values,0 to stop:'))
    if value == 0:
        break
    sum += value
    product *= value
    count += 1
    average = sum / count
print(F'Sum:{sum}')
print(F'Product:{product}')
print(F'Count:{count}')
print(F'Average:{average}')
