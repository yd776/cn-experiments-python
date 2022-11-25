import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1',9999))
s.listen(5)
print("listening")

def receiver(c) :
    while True:
            rmsg = c.recv(1024).decode()
            print("Client : "+rmsg)
            if rmsg == "x" :
                c.close()
                break

def sender(c) :
    while True:
            msg = input("Server : ").encode()
            c.send(msg)
            if msg == 'x':
                c.close()
                break

while True:
    c, addr = s.accept()
    
    lsn = threading.Thread(target=receiver, args=(c,))
    spk = threading.Thread(target=sender, args=(c,))

    lsn.start()
    spk.start()

    lsn.join()
    spk.join()
