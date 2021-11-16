import socket
 
sc = socket.socket()
adr='192.168.1.8'
port=1199

print(f'Starting server on {adr}')
sc.bind((adr, port))

print(f'Start listening {port}')

sc.listen(1)

while True:
    conn, rAdr = sc.accept()
    print(f'connected to {rAdr}')
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f"Sent reply to {rAdr}")
            conn.send(data.upper())
    except:
        print(f"Client {rAdr} Disconnected")
        pass
