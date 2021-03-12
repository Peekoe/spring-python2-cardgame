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
    # wait for a connection
    print ('waiting for connection 1')
    connection1, client_address1 = sock.accept()

    print ('Connection 1 confirmed!\nwaiting for connection 2')

    connection2, client_address2 = sock.accept()
    print('Connection 2 confirmed!')

    try:
        # show who connected to us
        print ('connection from', client_address1, client_address2)

        # receive the data in small chunks and print it
        while True:
            # initial player 1 messages
            connection1.send("Connection successful".encode(FORMAT))
            connection1.send("enter input...".encode(FORMAT))
            # player 2 waits...
            connection2.send("Wait for Player 1's input...".encode(FORMAT))
            # player 1 input
            player1_choice = connection1.recv(64).decode(FORMAT)
            print(player1_choice)
            # player 2 second message and input
            connection2.send("Player 1 done, enter input...".encode(FORMAT))
            player2_choice = connection2.recv(64).decode(FORMAT)
    finally:
        break
    # Clean up the connection
    connection1.close()
    connection2.close()