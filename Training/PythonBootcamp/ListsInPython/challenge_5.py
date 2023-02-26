# Write a program that prompts the user for a long string containing multiple words
# separated by whitespaces and
# prints back the same string with the words in backward order
my_str = input('Enter a sentence:')
string_as_list = my_str.split()
print(' '.join(string_as_list[::-1]))
