# Given the string s1, write a program to return the sum
# and the average of the digits that appear in the string, ignoring all other characters.

s1 = input("Enter a mixture of numbers and letters:")
s2 = '0123456789'
sum = 0
count = 0
for i in s1:
  if i in s2:
    x = int(i)
    count += 1
    sum += x
    average = sum/count
print(F'The sum of the numbers in your entry is:{sum} and the average is:{average:.3f} ')