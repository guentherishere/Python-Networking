#!/usr/bin/python3

import socket
# regular expression (re) library
import re

# Banner is a chunk of text that displays maybe the server name, application name. Useful in recon
# Can also use http library to do this. Will experiment w. that method later on

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("www.mattguenther.com", 80))

http_get = b"GET / HTTP/1.1\nHost: www.mattguenther.com\n\n"
data = ''
try:
    sock.sendall(http_get)
    data = sock.recvfrom(1024)
except socket.error:
    print ("Socket error", socket.errno)
finally:
    print("closing connection")
    sock.close()

strdata = data[0].decode("utf-8")
#  looks like one long line so split it at newline into multiple strings
headers = strdata.splitlines()
#  use regular expression library to look for the one line we like
for s in headers:
    if re.search('Server:', s):
        s = s.replace("Server: ", "")
        print(s)
