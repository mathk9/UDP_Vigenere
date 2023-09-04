from socket import *
from Vigenere import Vigenere

serverName = "192.168.0.51" # IPv4 // ::1 IPv6
serverPort = 12500
clientSocket = socket(AF_INET, SOCK_DGRAM) # AF_INET6
print("UDP Client\n")

while 1:
    message = input("\nInput message: ")

    if message == "exit":
        break
    else:
        palavraChave = input("\nInput key: ")
        vigenere_crypt = Vigenere()

        message = vigenere_crypt.vigenere_encrypt(message, palavraChave)        
        print("\nmessage: "+message+"\n")

    clientSocket.sendto(bytes(message,"utf-8"), (serverName, serverPort))

clientSocket.close()
