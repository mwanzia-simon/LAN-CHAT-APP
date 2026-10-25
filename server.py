import socket

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

print("TCP socket created succesifully!")

server_socket.bind(("0.0.0.0",5600))

server_socket.listen()

client_socket,client_address = server_socket.accept()
print(f"Connected to: {client_address}")

while True:
    message = client_socket.recv(1024)
    
    if not message:
        break
    print(f"Client says: {message.decode()}")
    reply = input("YOU (SERVER): ")
    client_socket.send(reply.encode())


print("Client Disconnected!")
client_socket.close()
server_socket.close()
print("Server shut down!")