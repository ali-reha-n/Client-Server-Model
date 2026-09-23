#The author of this code is Muhammad Talal Tahir.
#The purpose of this code is to create a TCP client which sends the message to server 
#and receives the message

import socket
import time
from datetime import datetime

SERVER_IP = "10.7.34.229"   # PUT SERVER REAL IP
SERVER_PORT = 12000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   
client.connect((SERVER_IP, SERVER_PORT))  

#starting time
start = time.time()
print('Starting Timestamp:' ,datetime.now())


client.send(b"hello there")
data = client.recv(1024)
print("SERVER SAY:", data.decode())

end = time.time()
print('Ending Timestamp:' ,datetime.now())
RTT = (end - start)*1000

print('Round-Trip Time:', RTT, 'ms')

client.close()   # TCP NEED CLOSE, UDP DON'T CARE