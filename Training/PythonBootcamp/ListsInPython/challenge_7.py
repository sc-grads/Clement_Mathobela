# Write a Python program that accepts as input a sequence of words separated by one
# or more whitespaces and prints out the same words with the letters in reversed order. Do not use list comprehension.


my_seq = input("Enter a few words separated by whitespaces: ")
words = my_seq.split()
i = 0
for letter in words:
    words[i] = letter[::-1]
    i += 1
new_str = ' '.join(words)
print(new_str)