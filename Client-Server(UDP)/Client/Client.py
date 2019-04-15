import socket

port = 1200
serverName = ('127.0.0.1',port)


clientSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


messageToSend = "Hello Server"
clientSocket.sendto(str.encode(messageToSend),serverName)

msgFromServer = clientSocket.recvfrom(1024)
msg = "Messafe from Server {}".format(msgFromServer[0])
print(msg)