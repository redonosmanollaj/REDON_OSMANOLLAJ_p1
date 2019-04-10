from socket import*
from datetime import*
import random
from Methods import*

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
        talk_to_client(conn)
        conn.close()


# RECEIVING/SENDING  REQUESTS/RESPONSES  FROM/TO CLIENT
def talk_to_client(conn):
    #question = "Operacioni (IPADRESA, NUMRIIPORTIT, BASHKETINGELLORE, PRINTIMI, EMRIIKOMPJUTERIT, KOHA, LOJA, FIBONACCI, KONVERTIMI)?"
    # conn.send(str.encode(question))

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
    elif request == 'KOHA':
        conn.sendall(str.encode(KOHA()))
    elif request == 'LOJA':
        conn.sendall(str.encode(LOJA()))
    elif 'FIBONACCI' in request:
        conn.sendall(str.encode(FIBONACCI(request)))
   







print("MIRE SE VINI NE FIEK-TCP PROTOKOLLIN")
create_socket()
bind_socket()
accept_connection()







        





