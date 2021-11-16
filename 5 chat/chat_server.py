import socket
 
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
adr='192.168.1.8' , 1199
client = []
print(f'Starting server on {adr[0]}')
sock.bind(adr)

print(f'Start listening {adr[1]}')

while 1 :
    data , addres = sock.recvfrom(1024)
    print (addres[0], addres[1])
    if  addres not in client : 
             client.append(addres)
    for clients in client :
            if clients == addres : 
                continue
            sock.sendto(data,clients)
