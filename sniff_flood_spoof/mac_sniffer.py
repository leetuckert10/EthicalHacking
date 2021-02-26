#!/usr/bin/python3

import os
import sys
import subprocess
from termcolor import colored
import socket
from struct import *


"""
"""

protocol = {6: "TCP",
            8: "EGP",}

def fmt_mac(value):
    mac = "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" % (
            value[0],
            value[1],
            value[2],
            value[3],
            value[4],
            value[5])
    return mac


def get_protocol(key):
    return protocol.get(key, f"{key}: Undefined")

def main():
    subprocess.call('clear', shell=True)

    try:
        sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))
        while True:
            packet = sock.recvfrom(1024)
            packet = packet[0]

            # The Ether header is 14 bytes, 6 each for src and dst mac plus 2
            # for protocol. In this case, this is all we are interested in.
            ether_header = packet[:14]

            # This returns a tuple with three values in it: the src mac, the dst
            # mac, and the protocol.
            value = unpack('6s6sH', ether_header)
            proto = get_protocol(value[2])
            print(colored(f"src: {fmt_mac(value[0])}  " +
                    f"dst: {fmt_mac(value[1])}  " + 
                    f"proto: {proto}", 'green'))

    except socket.error as e:
        print(colored(f"{e}", 'red'))
    except KeyboardInterrupt:
        print(colored("\n\nExiting loop...", 'blue'))
    finally:
        sock.close()
        print(colored("Socket closed...", 'blue'))


if __name__ == "__main__":
    main()
