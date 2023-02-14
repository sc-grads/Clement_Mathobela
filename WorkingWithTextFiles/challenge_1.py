with open('macs.txt') as file:
    my_list = file.read().split()
    my_set = set(my_list)
    new_list = list()
    for i in my_set:
        if i not in new_list:
            new_list.append(i)
print(new_list)
