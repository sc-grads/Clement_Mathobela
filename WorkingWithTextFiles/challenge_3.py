# Create a Python script that removes all empty lines including those that contain only spaces from a file.
with open('file.txt') as file:
    content = file.read().splitlines()
    new_list = list()
    for i in content:
        if len(i) < 1:
            pass
        else:
            new_list.append(i)

    with open('new_file', 'w') as f:

        content = f.write(''.join(new_list))