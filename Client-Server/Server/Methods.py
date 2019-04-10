from random import*
import array

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

def PRINTIMI(request):
    response = request.replace("PRINTIMI"," ")
    return response.strip()


def EMRIIKOMPJUTERIT():
    return 0 

def KOHA():
    today = datetime.now()
    return today.strftime("%d.%m.%Y %I:%M:%S %p")

def LOJA():
    numbers = []
    for i in range(7):
        numbers.append(randint(1,49))
    return str(numbers)

def FIBONACCI(request):
    return 0

def KONVERTIMI():
    return 0 
