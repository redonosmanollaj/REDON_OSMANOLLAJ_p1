from socket import*

serverName = 'localhost'
port = 1200

serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind((serverName,port))

print('Serveri eshte duke degjuar ne portin ',str(port))

serverSocket.listen(5)

print('Serveri eshte duke pritur ndonje kerkese')


while True:
    connectionSocket, addr = serverSocket.accept()
    clientip, cport = connectionSocket.getpeername()
    print('Client ip is: ',clientip)
    print('Klienti u lidh ne serverin %s ne portin %s' %addr)
    
    fjalia = connectionSocket.recv(1024)
    print('Serveri ka marre nga klienti fjaline: ',fjalia.decode())

    fjaliaM = fjalia.upper()
    connectionSocket.send(fjaliaM)
    print('Dhe ka kthyer si pergjigje fjaline: ',fjaliaM.decode())
    

    connectionSocket.close()


