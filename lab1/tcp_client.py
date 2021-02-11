import socket


socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 5555

socket_client.connect((host, port)) # встановлення з'єднання
socket_client.setblocking(True)
message = data = "It'і message!\n" * 100000
socket_client.send(message.encode('utf-8'))
socket_client.close()