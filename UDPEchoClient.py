import socket


host ='203.250.137.174'
port = 9900
BUFF_SIZE = 128

sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = (host,port)

message = input("Enter message : ")
message = bytes(message, encoding = 'utf-8')

try:
    bytes_sent = sock.sendto(message,server_address)
    data, address = sock.recvfrom(BUFF_SIZE)
    print("Received form server : %s" %data.decode())


except Exception as e:
    print("Exception: %s" %str(e))
sock.close()


