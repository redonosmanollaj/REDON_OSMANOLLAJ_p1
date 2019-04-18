import sys
from socket import*

clientSocket = socket(AF_INET,SOCK_STREAM)

serverName = str(input("Emri i serverit: "))
port = int(input("Porti: "))

try:
    clientSocket.connect((serverName,port))
    print("Jeni lidhur me sukses me serverin "+"\'"+str(serverName)+"\'")
except error as msg:
    print("Nuk mund te lidheni me kete server! Error: "+str(msg))

while True:
    varReceive = clientSocket.recv(1024)
    varReceive = varReceive.decode()
    if varReceive.endswith("?") | varReceive.endswith(":"):
        print(varReceive)
        strInput = input("\n")
        clientSocket.sendall(str.encode(strInput))
        if strInput == 'PERFUNDO':
            sys.exit(1)
    else:
        print(str("\n======================================================================\n")+varReceive+str("\n======================================================================\n")) 

clientSocket.close()




