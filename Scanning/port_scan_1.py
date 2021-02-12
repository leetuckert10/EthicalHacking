#!/usr/bin/python3

import subprocess
import sys
from termcolor import colored
import socket as s


def port_scanner(host):
    s.setdefaulttimeout(.5)
    try:
        for port in range(1, 1000):
            sock = s.socket(s.AF_INET, s.SOCK_STREAM)
            address = (host, port)

            # connect_ex() does not raise an exception on the C-level connect call but
            # returns an error code or zero if successful.
            if sock.connect_ex(address) == 0:
                print(colored(f"Port {port} is open...", 'green'))

            sock.close()
    except KeyboardInterrupt:
        print(colored("You pressed Ctrl-C. Aborting...", 'red'))
        sys.exit()
    except socket.error:
        print(colored("Couldn't connect to server...", 'red'))
        sys.exit()


def main():
    subprocess.call('clear', shell=True)

    host = input(colored("Enter the IP of the host to scan: ", 'yellow'))
    # port = input(colored("Enter the port do scan: ", 'yellow'))
    port_scanner(host)

main()
