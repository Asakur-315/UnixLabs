from os import name
import threading
import socket
threads = []
sock = socket.socket()
adress= '192.168.1.8', 1199

class T(threading.Thread):
    conn=""
    rAdr = 0
    def __init__(self,conn,rAdr):
        self.conn = conn
        self.rAdr = rAdr
        threading.Thread.__init__(self)
    def run(self) :
        print(f'connected to {self.rAdr}')
        while 1:
            try:
                data = self.conn.recv(1024)
                print(f"Sent reply to {self.rAdr}")
                self.conn.send(data.upper())
            except:
                print(f"Connection to {self.rAdr} lost.")
                conn.close()
                break



sock.bind(adress)
print("Server started. Listening")

sock.listen(1)
while 1:
    conn, rAdr = sock.accept()
    threads.append(T(conn,rAdr))
    threads[len(threads) - 1].start()
    pass