# Write a Python program to get a string from a given string
# where all occurrences of its first character have been changed to '$',
# except the first character itself.
# Sample String: 'mama'
# Expected Result: 'ma$a'

my_string = input("Enter a word/sentence:")
my_char = my_string[0]
new_string = my_string[1:].replace(my_char, "$")
newest_string = my_char + new_string


print(newest_string)