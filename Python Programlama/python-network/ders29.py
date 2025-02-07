import socket

client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address=('localhost',12345)
client_socket.connect(server_address)

message="Hi Python Network Server!"
client_socket.send(message.encode())

data=client_socket.recv(1024)
print("Server in the data:",data.decode())

client_socket.close()