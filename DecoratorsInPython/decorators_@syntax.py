#################################
## Decorators - The @ Syntax
#################################

user = {'level': 'admin', 'username': 'root', 'id': 0}

# defining a decorator
def only_admin(func): # decorators wrap a function, modifying its behavior.
    def wrapper_only_admin(*args, **kwargs):
        if user['level'] == 'admin':
            return func(*args, *kwargs)
        else:
            raise PermissionError("You have no permission to remove the file!")

    return wrapper_only_admin


@only_admin   # @ or pie syntax
def remove_file(f):
    """
    It removes a file.
    """
    import os, os.path
    if os.path.isfile(f):
        os.remove(f)
        print(f'{f} removed!')
    else:
        print('Argument is not file!')



try:
    remove_file('a.txt')
except PermissionError as e:
    print(e)

# equivalent to following code and without @only_admin before remove_file() definition:
# try:
#     remove_file = only_admin(remove_file)
#     remove_file('a.txt')
# except PermissionError as e:
#     print(e)

