import socket


socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 5555

socket_client.connect((host, port)) # встановлення з'єднання

while True:
    message = input("Enter message from client:\n")
    socket_client.send(message.encode('utf-8'))
    if message == 'stop':
        socket_client.close()
        break
# server_responce = socket_client.recv(1024)
# print(server_responce.decode('utf-8'))
# server_message = socket_client.recv(1024)
# print(server_message.decode('utf-8'))
# socket_client.close()