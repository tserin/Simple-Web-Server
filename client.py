import socket

c=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 9999
c.connect((host, port))

