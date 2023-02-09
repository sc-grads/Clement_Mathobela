# get a string made of the first and the last 2 chars from a given string
# entered by the user.

my_string = input("Enter a word/sentence and I'll form a word made of the first and 2 last character:")

new_string1 = my_string[:1]
new_string2 = my_string[-2:]

new_string = new_string1 + new_string2

print(new_string)


