some_email = input('Enter an email address:')
valid_email = {'@', '.'}
invalid_email = '[]{}()$*'
for i in valid_email:
    if i in some_email and 6 <= len(some_email) <= 16:

        print('Valid email!')
    else:
        print('Invalid email!!!')

# not_permitted = '[]{}()$*'
# must_contain = '.@'
# while True:
#    email = input("Enter your email:")
#    if len(email) < 6 or len(email) > 16:
#        print('Invalid email length!')
#    elif not set(email).isdisjoint(set(not_permitted)):  # two sets are disjoint if they have no elements in #common
#        print('Invalid symbols in email!')
#    elif set(must_contain) & set(email) != set(must_contain):
#        print('Invalid email. Must contain . and @')
#    else:
#      print('Valid email!')
#      break
