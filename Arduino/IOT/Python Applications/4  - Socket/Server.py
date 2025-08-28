import socket
import time

# get local machine name
host = '192.168.43.86'
port = 9998

# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind to the port
serversocket.bind((host, port))

# queue up to 5 requests
serversocket.listen(5)
print ("Server Started")
while True:
    # establish a connection
    clientsocket,addr = serversocket.accept()
    print ("*"*50)
    print ("Client with address %s:  %s just connected" % (addr[0],addr[1]))
    print("Got a connection from %s" % str(addr))
    currentTime = time.ctime(time.time()) + "\r\n"
    print ("Sending ACK")
    print ("*"*50)
    #print (currentTime)
    clientsocket.send(currentTime.encode('ascii'))
    clientsocket.close()
