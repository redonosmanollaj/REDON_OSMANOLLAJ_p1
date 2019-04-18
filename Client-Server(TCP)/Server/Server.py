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
        port=12000

        serverSocket = socket(AF_INET,SOCK_STREAM)

    except socket.error as msg:
        print("Socket creation error: ",msg)

# BIND SOCKET
def bind_socket():
    try:
        global host
        global port
        global serverSocket

        serverSocket.bind((host,port))
        serverSocket.listen(NUMBER_OF_CLIENTS)

    except error as msg:
        print("Socket binding error "+str(msg)+"Retrying...")
        bind_socket()

# HANDLE CONNECTION
def handle_connection():
    while True:
        conn, addr = serverSocket.accept()
        print("Connection has been estabilished. IP: "+str(addr[0])+" Port: "+str(addr[1]))
        t=threading.Thread(target=talk_to_client, args=(conn,))
        t.start()
    conn.close()
 
    
# RECEIVING/SENDING  REQUESTS/RESPONSES  FROM/TO CLIENT
def talk_to_client(conn):
    s = str("\nZgjedh njerin nga operacionet: \nIPADRESA \nNUMRIIPORTIT \nBASHKETINGELLORE \nPRINTIMI \nEMRIIKOMPJUTERIT \nKOHA \nLOJA \nFIBONACCI \nKONVERTIMI (KilowattToHorsepower, HorsepowerToKilowatt, DegreesToRadians, RadiansToDegrees, GallonsToLiters, LitersToGallons) \nEKUACIONIKUADRATIK \nDITELINDJAIME \nPERFUNDO?")
    conn.sendall(str.encode(s))
    while True:
        
        try:
            request = conn.recv(1024)
            request = request.decode()
    
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

            conn.sendall(str.encode("Lidhja eshte ende e hapur, kerkesa e radhes eshte:"))
        except Exception as ex:
            conn.sendall(str.encode("Error! "+ex))





