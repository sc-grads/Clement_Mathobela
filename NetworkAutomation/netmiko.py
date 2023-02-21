from netmiko import  ConnectHandler

device = {
    'device_type':'cisco_ios',
    'host':'10.1.1.10',
    'password':'pass123',
    'port':22,  #optional, default 22
    'secret':'cisco',   #optional, default ''
    'verbose':True  #optional, default False
    }

connection = ConnectHandler(**device)
output = connection.send_command('sh ip int brief')
print(output)
connection.disconnect