my_str  = 'wlo1      Link encap:Ethernet  HWaddr b4:6d:83:77:85:f3'

# YOUR CODE STARTS HERE
new_my_str = [i for i in my_str.split() if i !=' ']

interface_mac = new_my_str[0]+'!'+new_my_str[-1]
print(interface_mac)
