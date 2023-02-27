with open('banking.txt') as file:
    content = file.read().splitlines()
    deposit = 0
    withdrawal = 0
    for i in content:
        tmp = i.split(':')
        if  tmp[0] == 'D':
            deposit += int(tmp[1])
        elif tmp[0] == 'W':
            withdrawal += int(tmp[1])
    balance = deposit - withdrawal
    print(balance)