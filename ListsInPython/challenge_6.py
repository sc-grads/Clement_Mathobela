# Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.
sequence = input('Enter a heyphen-separated sequence of words:')
my_list = sequence.split('-')
print('-'.join(sorted(my_list)))