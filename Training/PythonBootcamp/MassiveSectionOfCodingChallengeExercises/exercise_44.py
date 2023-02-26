# List of Words
words = ['Anna', 'Car', 'Civic', 'Screen', 'Level', 'Cat', 'Mom' ]

# YOUR CODE STARTS HERE

palindromes = list()
# for i in words:
#     if i.lower() == i[::-1].lower():
#         palindromes.append(i)
[palindromes.append(i) for i in words if i.lower() == i[::-1].lower()]

print(palindromes)