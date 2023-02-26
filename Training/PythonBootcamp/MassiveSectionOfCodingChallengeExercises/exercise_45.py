# Use whatever name for the functions's parameter
def reverse(my_string):
    """
    This function returns a new string with all characters reversed.
    """
    # YOUR CODE STARTS HERE
    new_string =  list(my_string)
    reversed_string = ''.join(new_string[::-1])
    return reversed_string

print(reverse('Python'))