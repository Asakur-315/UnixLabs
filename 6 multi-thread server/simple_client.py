import socket
import threading
sc = socket.socket()

def connect():
    try:
        sc.connect(('192.168.1.8', 1199))
        print('Connected to server')
    except:
        print('Connection failed')

class T(threading.Thread):
    def run(self):
        while 1:
            data = sc.recv(1024)
            if data:
                print('Recieved from server')
            print(data.decode())

connect()
recieveThread = T()
recieveThread.start()
while True:

    msgStr = input()

    while msgStr != 'exit':
        sc.send(msgStr.encode())
        print('Message sent to server')

        msgStr = input()
        if msgStr == 'exit':
            sc.close()
            print('Closing connection')
