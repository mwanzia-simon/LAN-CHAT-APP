import socket

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

print("TCP client socket created succesifully!")

client_socket.connect(("127.0.0.1",5600))
print("Connected to the server succesifully!")

while True:
    message = input("YOU: ")
    client_socket.send(message.encode())
    reply = client_socket.recv(1024)
    print("SERVER: ",reply.decode())