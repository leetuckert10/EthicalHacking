#!/usr/bin/python3

import os
import sys
import subprocess
from termcolor import colored
import socket
from struct import *


"""
35. Getting source/destination mac address from received packets: mac_sniffer.py.

This program is quite a bit different than the one in the tutorial. The tutorial
version will not run using Python3 and I don't make it a habit to use Python 2.

"""

proto_numbers = {
    8: "EGP",
    6: "TCP",
}


def get_proto(proto):
    return proto_numbers.get(proto, f"<{proto}> Undefined")


def fmt_mac(value):
    """Takes a hex byte array and formats it as a mac address."""

    mac = "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" % (
            value[0],
            value[1],
            value[2],
            value[3],
            value[4],
            value[5])
    return mac


def main():
    subprocess.call('clear', shell=True)

    try:
        sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))
        while True:
            packet = sock.recvfrom(1024)    # 1024 is buffer size, not number of ports
            packet = packet[0]

            # The Ether header is 14 bytes, 6 each for src and dst mac plus 2
            # for protocol. In this case, this is all we are interested in.
            ether_header = packet[:14]

            # This returns a tuple with three values in it: the src mac, the dst
            # mac, and the protocol.
            value = unpack('6s6sH', ether_header)
            proto = get_proto(value[2])
            print(colored(f"Source MAC: {fmt_mac(value[0])}\t" +
                    f"Destination MAC: {fmt_mac(value[1])}\t" + 
                    f"Protocol: {proto}", 'green'))

    except socket.error as e:
        print(colored(f"{e}", 'red'))
    except KeyboardInterrupt:
        print(colored("\n\nExiting loop...", 'blue'))
    finally:
        sock.close()
        print(colored("Socket closed...", 'blue'))


if __name__ == "__main__":
    main()

