import socket

host ='203.250.137.157'
port = 8080
BUFF_SIZE = 128
BACKLOG=5

conn_sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = (host,port)
conn_sock.bind(server_address)

conn_sock.listen(BACKLOG)

while True:
    print("waiting for requests...")
    data_sock, address = conn_sock.accept()
    print("echo request from %s port %s "%address)
    message = data_sock.recv(BUFF_SIZE)

    if message:
        print("recevied message: %s\n" %message.decode())

    request = "GET/HTTP/1.0 200 OK\r\nContent-Type:text/html\r\n\r\n<HTML><BODY><H1>Hello,World!</H1></BODY></HTML>"
    data_sock.send(request.encode())
    response = data_sock.recv(4096)
    print(response)


    data_sock.close()