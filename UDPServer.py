#The author of this program is Muhammad Talal Tahir.
#The purpose of this program is to create a UDP server which recieves 
#message from client and then capitalizes it and returns it to client.

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(("0.0.0.0", 12001))   
print("SERVER UP. WAITING...")

while True:
    data, client_addr = server.recvfrom(1024)
    msg = data.decode()
    print("GOT:", msg, "FROM", client_addr)
    reply = msg.upper()
    server.sendto(reply.encode(), client_addr)