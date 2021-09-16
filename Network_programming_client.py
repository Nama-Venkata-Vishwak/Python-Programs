#Client Program 
import socket # Nama Venkata Vishwak
PORT = 65432 
s = socket.socket(socket. AF_INET, socket.SOCK_STREAM) 
s.connect ((socket.gethostname(), PORT)) 
while True: 
  msg = input('>>> ') 
  s.send (msg.encode('utf-8'))
  if msg == "exit": 
    break
data = s.recv(1024)
print('Server>>> ' data.decode ("utf-8"))
print('\n') 
s.close()
