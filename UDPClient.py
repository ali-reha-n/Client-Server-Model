from socket import *
import time 
from datetime import datetime

#setting the server IP address and port number
server_ip = '10.7.34.166'
server_port = 12001

#creating a UDP/IPv4 socket
client_socket = socket(AF_INET, SOCK_DGRAM)

#taking the input message
sentence = input('Input lowercase sentence: ')

#starting time
start = time.time()
print('Starting Timestamp:' ,datetime.now())
client_socket.sendto(sentence.encode(), (server_ip, server_port))

modifiedSentence, serverAddress = client_socket.recvfrom(1024)
end = time.time()
print('Ending Timestamp:' ,datetime.now())
RTT = (end - start)*1000

print('From Server:', modifiedSentence.decode())
print('Address of Server:', serverAddress)
print('Round-Trip Time:', RTT, 'ms')

client_socket.close()
