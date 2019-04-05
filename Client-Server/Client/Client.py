import socket

serverName = '127.0.0.1'
port = 1200

clientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

clientSocket.connect((serverName,port))

varInput = input("Shkruaj nje fjali per serverin")

clientSocket.sendall(str.encode(varInput))

varReceive = clientSocket.recv(1024)

print('Nga serveri ka ardhur: ',varReceive.decode())

#varInput2 = input("Shkruaj nje fjali tjeter per serverin")
#clientSocket.sendall(str.encode(varInput2))
#varReceive2 = clientSocket.recv(1024)
#print('Nga serveri ka ardhur: ',varReceive2.decode())


clientSocket.close()




