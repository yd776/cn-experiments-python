
 #server
import socket
s=socket.socket()
port=9999
s.bind(('localhost',port))
s.listen()
print('listening')
while True:
    conn,addr=s.accept()
    filename=conn.recv(1024).decode()
    files=open(filename,'rb')
    filedata=files.read(1024)
    conn.send(filedata)
    conn.close()
    
#clientr
import socket
c=socket.socket()
c.connect(('127.0.0.1',9999))

filename=str(input("Enter file name"))
c.send(bytes(filename,'utf-8'))
filedata=c.recv(1024).decode()
print(filedata)
c.close()
