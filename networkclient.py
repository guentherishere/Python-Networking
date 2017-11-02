#!/usr/bin/python3

import socket

host='localhost'

mysock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr=(host,5555)
mysock.connect(addr)

try:
    # the 'b' indicates that this is an array of bytes instead of a python string
    # this is then sent into mysock.sendall
    msg=b"This is a test\n"
    mysock.sendall(msg)
except socket.errno as e:
    print("Socket error ", e)
finally:
    mysock.close()
