import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
host=socket.gethostname()
s.bind(hostname,9999)
while True:
  msg,addr=s.recvfrom(1024).decode()
  print(msg)
  s.close()
 

import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.sendto("my name is yashas".encode(),(socket.gethostname(),9999)
         
