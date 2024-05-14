import socket

SERVER_HOST ='127.0.0.1'
SERVER_PORT =9999 

client_socket = socket.socket()

client_socket.connect((SERVER_HOST, SERVER_PORT))

message = "Hello from the client!"
client_socket.send(message.encode())

response = client_socket.recv(1024).decode()
print(f"[*] Received message from server: {response}")

client_socket.close()