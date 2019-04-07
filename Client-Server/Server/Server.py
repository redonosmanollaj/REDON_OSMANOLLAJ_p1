from socket import*

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



def IPADRESA(conn):
    clientip, port = conn.getpeername()
    return "IP Adresa e klientit eshte: "+str(clientip) 


def NUMRIIPORTIT(conn):
    clientip, port = conn.getpeername()
    return "Klienti eshte duke perdorur portin "+str(port)

def BASHKETINGELLORE(request):
    vowels = 0
    consonants = 0
    word = request.replace("BASHKETINGELLORE"," ")

    for i in word:
        if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'
           or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
            vowels = vowels + 1
        elif i == ' ':
            vowels=vowels+0
        else:
            consonants = consonants + 1
    return "Teksti i pranuar permban "+str(consonants)+" bashketingellore"

def PRINTIMI():
    return 0

def EMRIIKOMPJUTERIT():
    return 0 

def KOHA():
    return 0

def LOJA():
    return 0 

def FIBONACCI():
    return 0 

def KONVERTIMI():
    return 0 


print("MIRE SE VINI NE FIEK-TCP PROTOKOLLIN")
create_socket()
bind_socket()
accept_connection()







        





