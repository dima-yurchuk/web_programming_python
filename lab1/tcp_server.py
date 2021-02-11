import socket
from datetime import datetime
import time


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost' #ip - адреса хоста
port = 5555 #номер порта

server_socket.bind((host, port)) # зв'язування ip адреси з номером порта
server_socket.listen(5)
print('The server is waiting for connection......')
# сервер послідовно приймає повідомлення від декількох клієнтів, тобто підключився 1
# клієнт, надіслав повідомленяя, відключився, підключився другий клінт і тд.
while True:
    client_socket, addr = server_socket.accept()
    client_message = client_socket.recv(1024)
    while client_message:
        # print('Client message:' + client_message.decode('utf-8'))
        client_message = client_socket.recv(1024)
    print("*********All data recieved!*****************")
    server_socket.close()
    break