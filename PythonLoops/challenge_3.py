# Write a Python program that counts and displays the vowels of a given string ignoring the letter case.
my_str = input('Enter something:').lower()
vowels = 'aeiou'
count = 0
for i in my_str:
    if i in vowels:
        count += 1
print(count)
