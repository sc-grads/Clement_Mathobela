def tail(my_file, n):
    with open(my_file, 'r') as f:
        content = f.read().splitlines()
        last = content[len(content) - n:]
        my_str = '\n'.join(last)
        return my_str


print('sample_file.txt', 5)
