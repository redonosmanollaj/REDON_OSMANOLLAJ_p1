from socket import*
from random import*
from datetime import*
import array
import math
from math import radians
from math import degrees
from math import sqrt
from math import pow

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
        if ((i >= 'A' and i <= 'Z') or (i >= 'a' and i <= 'z')):
            if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'
               or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U' or i == ' '):
                vowels = vowels + 1
            else:
                consonants = consonants + 1
    return "Teksti i pranuar permban "+str(consonants)+" bashketingellore"

def PRINTIMI(request):
        if len(request)>len("PRINTIMI"):
            response = request.replace("PRINTIMI"," ")
            return str(response.strip())
        else:
            return str("Nuk ka asgje per tu printuar!")



def EMRIIKOMPJUTERIT():
    try:
        computername = str(gethostname())
        return "Emri i kompjuterit eshte "+str(computername)
    except error as msg:
        return "Emri i kompjuterit nuk dihet!"

def KOHA():
    today = datetime.now()
    return today.strftime("%d.%m.%Y %I:%M:%S %p")

def LOJA():
    numbers = []
    for i in range(7):
        numbers.append(randint(1,49))
    return str(numbers)


def FIBONACCI(request):
        n = int(request.replace("FIBONACCI"," "))
        result = int(((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5)))
        return str(result)



def KONVERTIMI(request):
    splitedString = request.split()
    converter = splitedString[1]
    number = float(splitedString[2])
    
    if converter.lower() == "kilowatttohorsepower".lower():
        return str(number*1.341)
    elif converter.lower() == "horsepowertokilowatt".lower():
        return str(number/1.341)
    elif converter.lower() == "degreestoradians".lower():
        return str(radians(number))
    elif converter.lower() == "radianstodegrees".lower():
        return str(degrees(number))
    elif converter.lower() == "gallonstoliters".lower():
        return str(number*3.78541)
    elif converter.lower() == "literstogallons".lower():
        return str(number/3.78541)
    else:
        return str("Kerkesa eshte shkruar gabim!")


# METODA PER ZGJIDHJEN E EKUACIONIT KUADRATIK
def EKUACIONIKUADRATIK(a,b,c):

    determinant = pow(b, 2)-4*a*c
    if determinant >= 0 :
        root1 = (-b+sqrt(determinant))/(2*a)
        root2 = (-b-sqrt(determinant))/(2*a)
    if determinant > 0:
        return "Ekuacioni ka dy zgjidhje reale.\nZgjidhja 1: "+str(root1)+"\nZgjidhja 2: "+str(root2)
    elif determinant == 0:
        return "Ekuacioni ka nje zgjidhje reale. \nZgjidhja: "+str(root1)
    else:
        return "Ekuacioni nuk ka zgjidhje reale"


def DITELINDJAIME(conn):
    set1 = str("01 03 05 07\n" +
		       "09 11 13 15\n" +
		       "17 19 21 23\n" +
		       "25 27 29 31")

    set2 = str(" 02 03 06 07\n" +
				"10 11 14 15\n" +
				"18 19 22 23\n" +
				"26 27 30 31")

    set3 = str("04 05 06 07\n" +
			   "12 13 14 15\n" +
			   "20 21 22 23\n" +
			   "28 29 30 31")

    set4 = str("08 09 10 11\n" +
			   "12 13 14 15\n" +
			   "24 25 26 27\n" +
			   "28 29 30 31")

    set5 = str("16 17 18 19\n" +
			   "20 21 22 23\n" +
			   "24 25 26 27\n" +
			   "28 29 30 31")
    day = 0
    #SET1
    conn.sendall(str.encode(set1+"\nA eshte ditelindja juaj ne kete set (PO ose JO)?"))
    answer = conn.recv(1024)
    
    if answer.decode().lower() == 'po':
        day = day+1
    #SET2
    conn.sendall(str.encode(set2+"\nA eshte ditelindja juaj ne kete set (PO ose JO)?"))
    answer = conn.recv(1024)
    
    if answer.decode().lower() == 'po':
        day = day+2
    #SET3
    conn.sendall(str.encode(set3+"\nA eshte ditelindja juaj ne kete set (PO ose JO)?"))
    answer = conn.recv(1024)
    
    if answer.decode().lower() == 'po':
        day = day+4
    #SET4
    conn.sendall(str.encode(set4+"\nA eshte ditelindja juaj ne kete set (PO ose JO)?"))
    answer = conn.recv(1024)
    
    if answer.decode().lower() == 'po':
        day = day+8
    #SET5
    conn.sendall(str.encode(set5+"\nA eshte ditelindja juaj ne kete set (PO ose JO)?"))
    answer = conn.recv(1024)
    
    if answer.decode().lower() == 'po':
        day = day+16

    conn.sendall(str.encode("\nDitelindja juaj eshte me date "+str(day)+" !"))



