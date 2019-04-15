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

        serverSocket.sendto(str.encode("HELLO"),address)

        bytesAddressPair = serverSocket.recvfrom(1024)
        message=bytesAddressPair[0].decode()
        address = bytesAddressPair[1]
        print("Connection estabilished with "+str(address[0]+" on port "+str(address[1])))
        print("Message from client : "+message)
    














# RECEIVING/SENDING  REQUESTS/RESPONSES  FROM/TO CLIENT
def talk_to_client():
    while True:
        try:
            serverSocket.sendall(str.encode("Operacioni (IPADRESA, NUMRIIPORTIT, BASHKETINGELLORE, PRINTIMI, EMRIIKOMPJUTERIT, KOHA, LOJA, FIBONACCI, KONVERTIMI, EKUACIONIKUADRATIK, DITELINDJAIME, PERFUNDO)?"))
            bytesAddressPair = serverSocket.recvfrom(1024)
            address = bytesAddressPair[1].decode()
            request = bytesAddressPair[0].decode()
    
            if request == 'IPADRESA':
                conn.sendall(str.encode(IPADRESA(conn)))
            elif request == 'NUMRIIPORTIT':
                conn.sendall(str.encode(NUMRIIPORTIT(conn)))
            elif 'BASHKETINGELLORE' in request:
                conn.sendall(str.encode(BASHKETINGELLORE(request)))
            elif 'PRINTIMI' in request:
                conn.sendall(str.encode(PRINTIMI(request)))
            elif request == 'EMRIIKOMPJUTERIT':
                conn.sendall(str.encode(EMRIIKOMPJUTERIT()))
            elif request == 'KOHA':
                conn.sendall(str.encode(KOHA()))
            elif request == 'LOJA':
                conn.sendall(str.encode(LOJA()))
            elif 'FIBONACCI' in request:
                conn.sendall(str.encode(FIBONACCI(request)))
            elif 'KONVERTIMI' in request:
                conn.sendall(str.encode(KONVERTIMI(request)))
            elif request == 'EKUACIONIKUADRATIK':
                conn.sendall(str.encode("Ekuacioni kuadratik ka formen ax^2+bx+c.\nJepe vleren e a:"))
                a = conn.recv(1024)
                floatA = float(a.decode())
                conn.sendall(str.encode("Jepe vleren e b:"))
                b = conn.recv(1024)
                floatB = float(b.decode())
                conn.sendall(str.encode("Jepe vleren e c:"))
                c = conn.recv(1024)
                floatC = float(c.decode())
                conn.sendall(str.encode(EKUACIONIKUADRATIK(floatA,floatB,floatC)))
            elif request == 'PERFUNDO':
                clientip, port = conn.getpeername()
                conn.close()
                print("Connection with "+str(clientip)+":"+str(port)+" is closed!")
                sys.exit()
            elif request == 'DITELINDJAIME':
                DITELINDJAIME(conn)
            else:
                conn.sendall(str.encode("Kerkesa eshte jo valide! Provoni edhe nje here..."))

        except Exception as ex:
            conn.sendall(str.encode("Error! "+ex))


