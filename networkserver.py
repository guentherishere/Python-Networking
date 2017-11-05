#!/usr/bin/python3

# basic network server
import socket

# bytes expect to receivet
size = 512
host = ''
port = 9898
#  family = Internet, type = stream socket means TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#  we have a socket, we need to bind to an IP address and port
#  to have a place to listen on
sock.bind((host, port))
#  accept 5 queued listeners, so up to 5 people trying to communicate at any given point
sock.listen(5)
#  we can store information about the other end
#  once we accept the connection attempt
#  variable 'c' is the client connection with 'addr' being the remote address
c, addr = sock.accept()
#  specific connection open with the client
data = c.recv(size)
if data:
    f = open("storage.dat", '+w')
    print("connection from: ", addr[0])
    f.write(addr[0])
    f.write(":")
    #  Data is a string of bytes and we want to write this to an actual character string
    f.write(data.decode("utf-8"))
    f.close()
sock.close()
