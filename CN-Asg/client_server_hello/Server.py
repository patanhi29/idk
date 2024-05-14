import socket

SERVER_HOST ='127.0.0.1'
SERVER_PORT =9999 

server_socket=socket.socket()

server_socket.bind((SERVER_HOST,SERVER_PORT))

server_socket.listen(1)

print(f"[*] Server listening on {SERVER_HOST}:{SERVER_PORT}")

client_socket, client_address = server_socket.accept()

print(f"[*] Accepted connection from {client_address[0]}:{client_address[1]}")

data = client_socket.recv(1024).decode()
print(f"[*] Received message from client: {data}")

response = "Hello from the server!"
client_socket.send(response.encode())

client_socket.close()
server_socket.close()