import socket

server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address=('localhost',12345)
server_socket.bind(server_address)
server_socket.listen(1)

print("Server calling start !")

while True:
    print("Connection waiting...")
    client_socket,client_address=server_socket.accept()
    print("Connection accepted OK ! ",client_address)
    
    data=client_socket.recv(1024)
    print("Client in Transfer data:",data.decode())
    
    message="Hi Client !"
    client_socket.send(message.encode())
    
    client_socket.close()
    break   
    