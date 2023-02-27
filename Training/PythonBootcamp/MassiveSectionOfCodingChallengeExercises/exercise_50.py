# YOUR CODE SATRTS HERE
with open('show_arp.txt') as file:
    content = file.read().splitlines()
    content = content[1:]
    ip_mac = []
    for i in content:
        ip = i.split()[1]
        mac = i.split()[3]

        ip_mac.append((ip, mac))