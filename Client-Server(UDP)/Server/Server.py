from socket import*
import random
from Methods import*
from math import radians
from math import degrees
from math import sqrt
import threading
import sys

NUMBER_OF_CLIENTS = int(10)

# CREATE SOCKET
def create_socket():
    try:
        global host 
        global port 
        global serverSocket
        host=""
        port=1200

        serverSocket = socket(AF_INET,SOCK_DGRAM)

    except socket.error as msg:
        print("Socket creation error: ",msg)

# BIND SOCKET
def bind_socket():
    try:
        global host
        global port
        global serverSocket

        serverSocket.bind((host,port))

    except error as msg:
        print("Socket binding error "+str(msg)+"Retrying...")

# HANDLE CONNECTION
def handle_connection():
    while True:
        bytesAddressPair = serverSocket.recvfrom(1024)
        message=bytesAddressPair[0].decode()
        address = bytesAddressPair[1]

        talk_to_client(message,address)

   

# RECEIVING/SENDING  REQUESTS/RESPONSES  FROM/TO CLIENT
def talk_to_client(request,address):
   # while True:
      #  try:
    
            if request == 'IPADRESA':
                serverSocket.sendto(str.encode("IP Adresa e klientit eshte: "+address[0]),address)
            elif request == 'NUMRIIPORTIT':
                serverSocket.sendto(str.encode("Klienti eshte duke perdorur portin "+str(address[1])),address)
            elif 'BASHKETINGELLORE' in request:
                serverSocket.sendto(str.encode(BASHKETINGELLORE(request)),address)
            elif 'PRINTIMI' in request:
                serverSocket.sendto(str.encode(PRINTIMI(request)),address)
            elif request == 'EMRIIKOMPJUTERIT':
                serverSocket.sendto(str.encode(EMRIIKOMPJUTERIT()),address)
            elif request == 'KOHA':
                serverSocket.sendto(str.encode(KOHA()),address)
            elif request == 'LOJA':
                serverSocket.sendto(str.encode(LOJA()),address)
            elif 'FIBONACCI' in request:
                serverSocket.sendto(str.encode(FIBONACCI(request)),address)
            elif 'KONVERTIMI' in request:
                serverSocket.sendto(str.encode(KONVERTIMI(request)),address)
            elif request == 'EKUACIONIKUADRATIK':
                serverSocket.sendto(str.encode("Ekuacioni kuadratik ka formen ax^2+bx+c.\nJepe vleren e a:"),address)
                bytesAddressPair = serverSocket.recvfrom(1024)
                a = bytesAddressPair[0]
                floatA = float(a.decode())
                serverSocket.sendto(str.encode("Jepe vleren e b:"),address)
                bytesAddressPair = serverSocket.recvfrom(1024)
                b = bytesAddressPair[0]
                floatB = float(b.decode())
                serverSocket.sendto(str.encode("Jepe vleren e c:"),address)
                bytesAddressPair = serverSocket.recvfrom(1024)
                c = bytesAddressPair[0]
                floatC = float(c.decode())
                serverSocket.sendto(str.encode(EKUACIONIKUADRATIK(floatA,floatB,floatC)),address)
            elif request == 'PERFUNDO':
                sys.exit()
            elif request == 'DITELINDJAIME':
                DITELINDJAIME(serverSocket,address)
            else:
                serverSocket.sendto(str.encode("Kerkesa eshte jo valide! Provoni edhe nje here..."),address)
        #except Exception as ex:
         #   serverSocket.sendto(str.encode("Error! "+ex),address)


