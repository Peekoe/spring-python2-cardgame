import socket
import api
import time
import pickle
FORMAT = 'utf-8'

# create TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# retrieve local hostname
local_hostname = socket.gethostname()

# get fully qualified hostname
local_fqdn = socket.getfqdn()

# get the according IP address
ip_address = socket.gethostbyname(local_hostname)

# bind the socket to the port 23456, and connect
server_address = (ip_address, 23456)
sock.connect(server_address)
print(sock.recv(256).decode(FORMAT))

# get message
i = api.create_monster(api.data)
message = pickle.dumps(i)

def monster_stats(i):
    print(i.name)
    print(i.attributes)
    print(i.type)
    print(i.atk)
    print(i._def)
    print(i.description)
    print(i.effects)

# send out to server
while sock.recv(256).decode(FORMAT) != 'ready':
    time.sleep(0.1)

sock.sendall(message)
otherClient = sock.recv(256)
monster_stats(pickle.loads(otherClient))

# close connection
while sock.recv(256).decode(FORMAT) != 'done':
    time.sleep(0.1)

sock.close()

