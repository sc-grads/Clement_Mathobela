def counter(my_str):
    vowels = 'aeiou'
    my_vowels = 0

    my_str = my_str.lower()

    for char in vowels:
        my_vowels += my_str.count(char)

    my_consonants = len(my_str) - my_vowels

    return (my_vowels, my_consonants)