import socket

serverName = '127.0.0.1'
port = 1200

clientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

clientSocket.connect((serverName,port))

while True:
    varInput = input("Operacioni (IPADRESA, NUMRIIPORTIT, BASHKETINGELLORE, PRINTIMI, EMRIIKOMPJUTERIT, KOHA, LOJA, FIBONACCI, KONVERTIMI)?")

    clientSocket.sendall(str.encode(varInput))

    varReceive = clientSocket.recv(1024)

    print(varReceive.decode())



clientSocket.close()




