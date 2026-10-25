import socket

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

print("TCP client socket created succesifully!")


client_socket.connect(("127.0.0.1",5600))
print("Connected to the server succesifully!")

message = "Hello from the client!"
client_socket.send(message.encode())