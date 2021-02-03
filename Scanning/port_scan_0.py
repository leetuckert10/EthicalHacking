#!/usr/bin/python

import socket

socket.setdefaulttimeout(2)
#                  IPV4      TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = raw_input("Enter the IP of the host to scan: ")

def port_scanner(port):
    if sock.connect_ex((host, port)):
        print "Port %d is closed..." % (port)
    else:
        print "Port %d is open..." % (port)

for port in range(440, 450):
    port_scanner(port)

