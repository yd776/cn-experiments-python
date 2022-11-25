#server.py

import socket
import time
s=socket.socket()
host=socket.gethostname()
port=9999
s.bind((host,port))
s.listen(5)
while True:
    cmnd,addr=s.accept()
    ct=time.ctime(time.time())
    cmnd.send(ct.encode('ascii'))
    cmnd.close()
    
    


# client.py  
import socket

s = socket.socket() 
# get local machine name
host = socket.gethostname()                           
port = 9999

s.connect((host, port))                               

tm = s.recv(1024)                                     
s.close()
print("The time got from the server is %s" % tm.decode('ascii'))
