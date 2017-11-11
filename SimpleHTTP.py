#!/usr/bin/python3

import http.client

# instance of http connection option
h = http.client.HTTPConnection("www.google.com")
# the '/' indicates we want the index page from the top level directory
h.request("GET", "/")
data = h.getresponse()
print (data.code)
print (data.headers)
text = data.readlines()
for t in text:
    print(t.decode('utf-8'))
