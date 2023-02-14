

with open('devices.txt') as file:
    content = file.read().splitlines()
    my_list = list()
    for i in content[1:]:
        my_list.append(i.split(':'))
    print(my_list)





