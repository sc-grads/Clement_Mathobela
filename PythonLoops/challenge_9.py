# Write a Python program that finds the common #characters that appear in
# two given strings.
my_string1 = input('Enter a word/sentence:')
my_string2 = input("Enter a 2nd word/sentence:")
my_string3 = ''
for i in my_string1:
    if i in my_string2:
        my_string3 = my_string3 + i
print(my_string3)
