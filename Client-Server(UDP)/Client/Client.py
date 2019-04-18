import socket
import sys

ip = input("Emri i serverit: ")
port = int(input("Porti: "))

serverName = (ip,port)

clientSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s = str("\nZgjedh njerin nga operacionet: \nIPADRESA \nNUMRIIPORTIT \nBASHKETINGELLORE \nPRINTIMI \nEMRIIKOMPJUTERIT \nKOHA \nLOJA \nFIBONACCI \nKONVERTIMI \nEKUACIONIKUADRATIK \nDITELINDJAIME \nPERFUNDO?")
print(s)
while True:

    strInput = input()
    clientSocket.sendto(str.encode(strInput),serverName)
    if strInput == 'PERFUNDO':
        sys.exit()
    msgFromServer = clientSocket.recvfrom(1024)
    msg = format(msgFromServer[0].decode())
    if msg.endswith("?") | msg.endswith(":"):
        print(msg)
    else:
        print(str("\n======================================================================\n")+msg+str("\n======================================================================\n"))