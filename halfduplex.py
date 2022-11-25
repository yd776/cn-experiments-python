
#server

import socket

server_port=5000
s=socket.socket()
s.bind(('',server_port))
s.listen(1)
print("WELCOME SERVER READY TO RECEIVE")
conn,addr=s.accept()
while True:
  sentence=conn.recv(2048).decode()
  print(sentence)
  message=input(">>")
  conn.send(message.encode())
  if(message=="q"):
    conn.close()



#clientq
import socket
s=socket.socket()
host=5000
s.connect(('localhost',5000))
while True:
  sentence=input(">>")
  s.send(sentence.encode())
  message=s.recv(2048)
  print(message.decode())
  if(sentence=='q'):
    s.close()
