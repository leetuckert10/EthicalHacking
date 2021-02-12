#!/usr/bin/python3

import sys
import subprocess
from termcolor import colored
import socket as s


def get_banner(ip, port):
    s.setdefaulttimeout(1)
    banner = None
    try:
        sock = s.socket(s.AF_INET, s.SOCK_STREAM)
        address = (ip, port)

        sock.connect(address)
        banner = sock.recv(1024)
    except s.error:
        pass
    finally:
        sock.close()
    return banner


def main():
    subprocess.call('clear', shell=True)
    print(colored("In main()", 'yellow'))
    ip = input(colored("Enter the IP address: ", 'blue'))

    for port in range(1, 101):
        banner = get_banner(ip, port)
        if banner:
            # For some reason the telnet port on metasploit throws a
            # UnicodeDecodeError so I had to wrap it in a try block.
            try:
                banner = banner.decode()
            except UnicodeDecodeError:
                pass
            print(colored(f"{port}/tcp returned: {banner}", 'green'))


main()
