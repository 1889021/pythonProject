import socket

host ='203.250.137.157'
port = 10999
BUFF_SIZE = 128
BACKLOG=5

conn_sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = (host,port)
conn_sock.bind(server_address)

conn_sock.listen(BACKLOG)

while True:
    message = input("Enter message:")
    if message.upper()=='QUIT':
        break
    print("waiting for requests...")
    data_sock, address = conn_sock.accept()
    print(data_sock)
    print("echo request from{} port{}".format(address[0].address[1]))

    message = data_sock.recv(BUFF_SIZE)
    while message:

        print("recevied message: {}" .format (message.decode()))
        data_sock.sendall(message)
        message = data_sock.recv(BUFF_SIZE)

        data_sock.close()