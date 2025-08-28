# client.py
import socket

# get local machine name
host = '192.168.43.86'
port = 9998

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connection to hostname on the port.
s.connect((host, port))

# Receive no more than 1024 bytes
tm = s.recv(1024)
#s.sendall("Hello")
s.close()
print ("*"*50)
print("The time got from the server is %s" % tm.decode('ascii'))
print ("*"*50)

