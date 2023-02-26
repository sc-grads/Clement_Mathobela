my_string = input("Enter a palindrome:")
new_string = my_string.replace(' ','').lower()

newest_string = new_string[::-1]

print("Is", my_string, "a palindrome?", new_string == newest_string)