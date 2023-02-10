

import random
import string

name = input('Enter your name:')
password_length = int(input(F'Hi {name},How many characters would you like your password to have? :'))

characters = string.ascii_letters + string.punctuation
password = ''
for _ in range(password_length):
    random_char = random.choice(characters)
    password += random_char
print(F'Your random Password is: {password}', end='')