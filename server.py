import socket
import time
host ='203.250.137.157'
port = 9900
BUFF_SIZE = 1024

sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = (host,port)
sock.bind(server_address)


while True:
    print("Waiting for request...")

    message, client_address = sock.recvfrom(BUFF_SIZE)
    print("echo request form %s port %s" % client_address)

    sock.sendto(message, client_address)

sock.close()


