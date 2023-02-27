# Write a Python script that tests if a string is a palindrome.

my_string = input("Enter a palindrome:")

new_string = my_string[::-1]

print("Is", my_string, "a palindrome?", my_string == new_string)


