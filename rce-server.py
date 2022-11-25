import socket
import subprocess

s = socket.socket()
s.bind(('127.0.0.1', 9999))
s.listen(5)
print("Listenting..")

while True:
    c, ad = s.accept()
    cmd = c.recv(1024).decode()
    rep = subprocess.check_output(cmd, shell=True)
    print(rep.decode())
    c.send(rep)
    c.close()
    print("execution completed")