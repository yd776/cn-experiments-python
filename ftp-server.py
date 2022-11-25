import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 9999))
s.listen(5)
print("listening..")

while True:
    c, addr = s.accept()
    print(addr)
    fn = c.recv(1024)
    f = open(fn, 'r')
    fc = f.read()
    c.send(fc.encode())
    c.close()
    print("file : " + fc)