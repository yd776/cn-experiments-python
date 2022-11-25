import socket
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(('127.0.0.1', 9999))
print("connected")
while True:
    msg = input("Client : ")
    c.send(msg.encode())
    if(msg == 'x'):
        break
    print("Server : " + c.recv(1024).decode())

c.close()