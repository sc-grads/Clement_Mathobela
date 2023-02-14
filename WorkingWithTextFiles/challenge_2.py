with open('sample_file.txt') as file:
    my_list = ' '.join(file.read().split())
print(my_list)
