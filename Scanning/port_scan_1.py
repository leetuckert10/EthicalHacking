#!/usr/bin/python3

import socket as s

#                  IPV4      TCP
sock = s.socket(s.AF_INET, s.SOCK_STREAM)
host = "192.168.1.10"
port = 449

def port_scanner(port):
    print(f"Scanning port {port}")
    if sock.connect_ex((host, port)):
        print(f"port {port} is closed...")
    else:
        print(f"port {port} is open...")

def main():
    port_scanner(port=port)

main()
