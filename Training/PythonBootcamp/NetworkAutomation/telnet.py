import telnetlib
import time

host = '10.1.1.10'
port = '23'
user = 'user1'
password = 'pass123'

tn = telnetlib.Telnet(host=host,port=port)

tn.read_until(b'Username:')
tn.write(user.encode()+b'\n')

tn.write(b'terminal length 8 \n')
tn.read_until(b'Password:')
tn.write(password.encode() + 'b \n')

tn.write(b'Show ip interface brief \n')
tn.write(b'exit\n')
time.sleep(2)

output = tn.read_all()
print(type(output))
output = output.decode()
print(output)