my_str = 'wlo1 Link encap:Ethernet HWaddr b4:6d:83:77:85:f3'

# Write a Python script that extracts the MAC address(b4:6d:83:77:85:f3) from the string.

print(my_str.find('b'))  # find the index of b

mac_address = my_str[32:]  # slice from b to the end of the string
print(mac_address)
