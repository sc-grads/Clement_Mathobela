# Write a Python script that finds all occurrences of a substring in a given string
# by ignoring the letter case.

my_string = input("Enter a sentence:")
my_substring = input("Enter a word and i will tell you if it was in your sentence:")
sentence = my_string.lower()
word = my_substring.lower()
print( my_substring, "was in my sentence:",word in sentence)