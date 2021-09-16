#Server Program 
import socket #Nama Venkata Vishwak  
PORT = 65432 
s = socket.socket (socket.AF_INET, socket. SOCK_STREAM) 
s.bind((socket.gethostname(),PORT)) 
s.listen(5) 
c, addr = s.accept()
print('Got connection from', addr)
while True:
  data = c.recv(1024).decode ('utf-8')
  inputs = data.split()
  print (data.upper())
  if data=="exit":
    print("Disconnecting")
    break 
if inputs[0]=="print": 
  C.send (data[6::].encode ('utt-8')) 
  print ("Successful")
else: 
  c.send ('Unknown Command'.encode ('utf-8')) 
s.close ()
