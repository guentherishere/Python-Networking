#!/usr/bin/python

import pcapy

devices = pcapy.findalldevs()
print(devices)

#  eth0 = device, 65536 = # of byte to capture per packet, 1 = promiscuous mode, 0 = timeout (ms)
cap = pcapy.open_live("eth0", 65536 , 1 , 0)

count = 1
while count:
    # cap.next gives next packet in the stream and we will get the header and payload from that packet
    (header, payload) = cap.next()
    print(count)
    count = count + 1
