import socket
from datetime import datetime


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost' #ip - адреса хоста
port = 5555 #номер порта

server_socket.bind((host, port)) # зв'язування ip адреси з номером порта
server_socket.listen(5)
print('The server is waiting for connection......')

clientsocket, addr = server_socket.accept()
client_message = clientsocket.recv(1024)
print('Client message:' + client_message.decode('utf-8') +
      "\nTime to receive the message:" + str(datetime.now()))

server_socket.close()