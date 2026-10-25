# Importing the built-in networking module
import socket

# Creating the socket
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# server_socket - variable
#  socket.socket() - creates a new socket
# socket.AF_INET - Tells python we are going to use IPV4 addresses
# socket.SOCK_STREAM - selects a stream socket which well use for TCP

print("TCP socket created succesifully!")

# Binding the server to an IP address and Port
server_socket.bind(("127.0.0.1",5600))

server_socket.listen()

client_socket,client_address = server_socket.accept()
print(f"Connected to: {client_address}")


client_socket.close()
server_socket.close()