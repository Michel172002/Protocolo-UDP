import socket

def Main():
    # Endereco IP do Servidor
    ip_server = "127.0.0.1"
    # Porta em que o servidor estara ouvindo
    port = 12000

    #  socket.SOCK_DGRAM=usaremos UDP
    udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    #Destino
    dest = (ip_server, port)

    print("Digite algo: ")   
    # Mensagem recebera dados do teclado      
    msg = input()
    # enviar a mensgem para o destino(IP + porta)
    udp_client.sendto(bytes(msg,"utf8"), dest)

    udp_client.close()


if __name__ == '__main__':
    Main()