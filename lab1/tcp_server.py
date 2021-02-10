import socket
from datetime import datetime
import time
import sys


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost' #ip - адреса хоста
port = 5555 #номер порта

server_socket.bind((host, port)) # зв'язування ip адреси з номером порта
server_socket.listen(5)
print('The server is waiting for connection......')
client_socket, addr = server_socket.accept()
while True:
    # client_socket, addr = server_socket.accept()
    # print('Got a connection from {}'.format(addr))
    # clientsocket.send('What is your name?'.encode('utf-8'))
    client_message = client_socket.recv(1024)
    if client_message.decode('utf-8') == 'stop':
        server_socket.close()
        break
    print('Client message:' + client_message.decode('utf-8') +
      "\nTime to receive the message:" + str(datetime.now()))
# time.sleep(5)
# client_socket.send(client_message)

# server_socket.close()