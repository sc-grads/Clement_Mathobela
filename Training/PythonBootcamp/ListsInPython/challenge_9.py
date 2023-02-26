# Create a Python script that calculates and displays the number of occurrences of each element of a list.
my_list = list(input('Enter a word/sentence:'))
some_list = list()
for item in my_list:
    some_list.append(item)
    occurences = my_list.count(item)

    if item not in some_list:
        continue
    print(F'{item}--->{occurences}')