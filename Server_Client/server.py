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

# output hostname, domain name and IP address
print ("working on %s (%s) with %s" % (local_hostname, local_fqdn, ip_address))

# bind the socket to the port 23456
server_address = (ip_address, 23456)
print ('starting up on %s port %s' % server_address)
sock.bind(server_address)

# listen for incoming connections (server mode) with one connection at a time
sock.listen(2)

while True:
    print ('waiting for connection 1')
    connection1, client_address1 = sock.accept()
    print ('Connection 1 confirmed!')

    print ('waiting for connection 2')
    connection2, client_address2 = sock.accept()
    print ('Connection 2 confirmed!')

    try:
        # show who connected to us
        print ('connection from', client_address1)
        print ('connection from', client_address2)
        connection1.send("Connection successful".encode(FORMAT))
        connection1.send("enter input...".encode(FORMAT))
        connection2.send("Connection successful".encode(FORMAT))
        connection2.send("enter input...".encode(FORMAT))

        # player 1 input
        client1_msg = connection1.recv(64).decode(FORMAT)
        connection2.send(client1_msg)
        # player 2 input
        client2_msg = connection2.recv(64).decode(FORMAT)
        connection1.send(client2_msg)

        print('client1 said', client1_msg)
        print('client2 said', client2_msg)
    finally:
        # Clean up the connection
        connection1.close()
        connection2.close()
