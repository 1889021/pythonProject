import socket

server_addr ='203.250.137.157'
server_port = 9000

sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM,0)
sock.connect((server_addr, server_port))
sock.send(b'Hello server')
ret_message =  sock.recv(100)
print(ret_message.decode())
print(sock)