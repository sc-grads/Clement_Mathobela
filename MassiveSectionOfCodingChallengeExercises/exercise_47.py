def vowel_count(my_str):
    """
    This function counts the number of vowels in a string and returns a dictionary.
    """
    vowels = 'aeiou'
    my_dict = dict()
    new_string = my_str.lower()
    ## YOUR CODE STARTS HERE
    for i in new_string:
        if i in vowels:
            # new_string.count('i')
            my_dict[i] = new_string.count(i)
    return my_dict
print(vowel_count('Hellooo'))