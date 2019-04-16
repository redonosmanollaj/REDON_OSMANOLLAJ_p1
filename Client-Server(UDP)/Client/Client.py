import socket

port = 1200
serverName = ('127.0.0.1',port)


clientSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s = str("Zgjedh njerin nga operacionet: \nIPADRESA \nNUMRIIPORTIT \nBASHKETINGELLORE \nPRINTIMI \nEMRIIKOMPJUTERIT \nKOHA \nLOJA \nFIBONACCI \nKONVERTIMI \nEKUACIONIKUADRATIK \nDITELINDJAIME \nPERFUNDO?")
print(s)
while True:

    clientSocket.sendto(str.encode(input()),serverName)

    msgFromServer = clientSocket.recvfrom(1024)
    msg = "Messafe from Server {}".format(msgFromServer[0].decode())
    print(msg)