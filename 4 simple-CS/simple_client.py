import socket

sc = socket.socket()

def connect():
    try:
        sc.connect(('192.168.1.8', 1199))
        print('Connected to server')
    except:
        print('Connection failed')


connect()
while True:

    msgStr = input()

    while msgStr != 'exit':
        sc.send(msgStr.encode())
        print('Message sent to server')
        data = sc.recv(1024)
        if data:
            print('Recieved from server')
        print(data.decode())
        msgStr = input()
        if msgStr == 'exit':
            sc.close()
            print('Closing connection')
