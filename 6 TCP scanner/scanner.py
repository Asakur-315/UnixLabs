import socket
import threading
import sys

ports = []

def scan_port(ip,port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    try:
        sock.connect((ip,port))
        ports.append(port)
        sock.close()
    except:
        pass



ip =  input("Адрес: ")
max = int (input("Сколько портов проверять? : "))
step = max // 40

sys.stdout.write("[%s]" % (" " * 40))
sys.stdout.flush()
sys.stdout.write("\b" * 41)

part = 0
for i in range(max):
    t1 = threading.Thread(target=scan_port, args=(ip,i))
    t1.start()

    if i > part:
        sys.stdout.write("-")
        sys.stdout.flush()
        part += step
sys.stdout.write("]\n")
print("done")
ports.sort()
for port in range(len(ports)):
    print(f'Порт {ports[port]} открыт')

input("Нажмите любую клавишу для выхода")