import socket

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
print(sock.recv(128).decode(FORMAT))

# get message
message = input("What would you like to say?").encode(FORMAT)

# send out to server
sock.sendall(message)
print(sock.recv(128).decode(FORMAT))
# close connection
sock.close()

