from socket import *

#deciding server port and sockets
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)


serverSocket.bind(('0.0.0.0',serverPort)) 
serverSocket.listen(1)
print('The server is ready to receive on port:', serverPort)

while 1:

    connectionSocket, addr = serverSocket.accept() 
    sentence = connectionSocket.recv(1024)

    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence)

    connectionSocket.close()
