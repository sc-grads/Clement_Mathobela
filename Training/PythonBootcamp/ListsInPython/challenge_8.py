# Create an alternative solution for the previous challenge using list comprehension.
my_seq = input("Enter a few words separated by whitespaces: ")
words = my_seq.split()

# reverse the letters in each word
words = [letter[::-1] for letter in words]

new_str = ' '.join(words)

print(new_str)