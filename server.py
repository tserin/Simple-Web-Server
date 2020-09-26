import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create socket
s.bind(('localhost', 8080))                  #bind the host and port
s.listen(3)                                           #listen to connection
print("Server starts")
while True:
    conn, addr =s.accept()
    print(f"Connection from {addr}")
    msg = conn.recv(1024)
    print(msg)
    filename ='hello.html'
    f = open(filename,'r')
    conn.sendall(str.encode("""HTTP/1.0 200 OK\n""", 'iso-8859-1'))
    conn.sendall(str.encode('Content-type: text/html\n', 'iso-8859-1'))
    conn.sendall(str.encode('\n'))
        #send data per line
    for l in f.readlines():
        print('sent', repr(l))
        conn.sendall(str.encode(""+l+"", 'iso-8859-1'))
        l=f.read(1024)
    f.close()





