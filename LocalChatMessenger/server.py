import socket
import os
from faker import Faker

socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

server_address = '/tmp/socket_file'

try:
    os.unlink(server_address)

except FileNotFoundError:
    pass

print('Starting up on {}'.format(server_address))

socket.bind(server_address)
socket.listen(1)

while True:
    connection, client_adress = socket.accept()
    try:
        print('connection from', client_adress)

        while True:
            data = connection.recv(16)
            data_str = data.decode('utf-8')

            print('Received: ' + data_str)

            if data:
                fake = Faker()
                text = fake.text()
                response =  text
                connection.sendall(response.encode())
            else:
                print('no data from ' + client_adress)
                break
    finally:
        print('Closing current connection')
        connection.close()