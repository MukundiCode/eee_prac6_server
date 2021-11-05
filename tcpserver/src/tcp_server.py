import socket
import sys

f = open("/data/sensorlog.txt", "w+")


TCP_IP = '0.0.0.0'
TCP_PORT = 5003
BUFFER_SIZE = 20  # Normally 1024, but we want fast response

newconnection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
newconnection.bind((TCP_IP, TCP_PORT))
newconnection.listen(1)

conn, addr = newconnection.accept()
print('Connection address:', addr)

#TODO: Add code to create a socket ready to recieve data



with newconnection:
    while True:
        data = conn.recv(1024)
        print('\nReceived', repr(data))
        f.write("\nReceived: ")
        f.write(repr(data))
        f.flush()
        if not data: break
