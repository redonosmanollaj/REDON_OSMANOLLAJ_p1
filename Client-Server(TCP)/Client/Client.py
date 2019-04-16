import socket

serverName = '127.0.0.1'
port = 12000

clientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

clientSocket.connect((serverName,port))

while True:
    varReceive = clientSocket.recv(1024)
    varReceive = varReceive.decode()
    print(varReceive) 
    if varReceive.endswith("?") | varReceive.endswith(":"):
        clientSocket.sendall(str.encode(input()))


clientSocket.close()




