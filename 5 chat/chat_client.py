import socket
import threading

sc = socket.socket()

def read_sok():
     while 1 :
         data = sor.recv(1024)
         print(data.decode('utf-8'))

adr = '192.168.1.8', 1199
name = input("Your name:")

sor = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sor.bind(('', 0))

sor.sendto((name+' connected to server').encode('utf-8'), adr)
potok = threading.Thread(target= read_sok)
potok.start()
while 1 :
    msg = input()
    sor.sendto(('['+name+']: '+msg).encode('utf-8'), adr)