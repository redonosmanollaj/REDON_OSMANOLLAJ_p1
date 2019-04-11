from socket import*
import random
from Methods import*
from math import radians
from math import degrees
from math import sqrt

# CREATE SOCKET
def create_socket():
    try:
        global host 
        global port 
        global serverSocket
        host=""
        port=1200

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
        serverSocket.listen(10)

    except socket.error as msg:
        print("Socket binding error "+str(msg)+"Retrying...")
        bind_socket()

# ACCEPT CONNECTION
def accept_connection():
    while True:
        conn, addr = serverSocket.accept()
        print("Connection has been estabilished. IP: "+str(addr[0])+" Port: "+str(addr[1]))
        while True:
             talk_to_client(conn)
    conn.close()


# RECEIVING/SENDING  REQUESTS/RESPONSES  FROM/TO CLIENT
def talk_to_client(conn):
    #question = "Operacioni (IPADRESA, NUMRIIPORTIT, BASHKETINGELLORE, PRINTIMI, EMRIIKOMPJUTERIT, KOHA, LOJA, FIBONACCI, KONVERTIMI)?"
    # conn.send(str.encode(question))
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
        else:
            conn.sendall(str.encode("Kerkesa eshte jo valide! Provoni edhe nje here..."))
    except:
        conn.sendall(str.encode("Kerkesa ka gabime sintaksore!  Ju lutem provoni edhe nje here!"))
   





print("Server is waiting to connect ...")
create_socket()
bind_socket()
accept_connection()







        





