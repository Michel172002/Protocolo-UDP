import socket
from random import sample

def Main():
    # Endereco IP do Servidor
    host = ""
    # Porta que o Servidor vai ouvir 
    port = 12000

    udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # faz o bind do ip e a porta para que possa comecar a ouvir
    udp_server.bind((host, port))

    #Recebe a mensagem que o cliente enviou e o endereco do cliente
    msg_receivedByte, end_client = udp_server.recvfrom(1024)

    #Decodifica a mensagem recebida em bytes para String
    msg_receivedString = msg_receivedByte.decode()

    ShuffledMsg(msg_receivedString)
    print("Endereço do cliente:", end_client)

    udp_server.close()

def ShuffledMsg(msg_receivedString):
    shuffled = sample(msg_receivedString, len(msg_receivedString))
    shuffled_msg = "".join(shuffled)
    print("Mensagem emmbaralhada do cliente: " + shuffled_msg)
    
if __name__ == '__main__':
    Main()