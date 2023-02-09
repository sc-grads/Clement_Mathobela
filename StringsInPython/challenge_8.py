# Write a Python program to remove the nth index character from a nonempty string.
my_string = input("Enter a word/sentence:")
char_index = int(float(input("Enter an index number:")))
character = my_string[char_index]
new_string = my_string.replace(character, "")
print(new_string)
