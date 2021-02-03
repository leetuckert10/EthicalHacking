#!/usr/bin/python3

import subprocess
import sys
from termcolor import colored
import socket as s
import threading
import ipaddress
import optparse


def connect_port(host, port):
    print(f"Thread {threading.current_thread} started for {host} on {port}...")
    try:
        port = int(port)
    except ValueError:
        print(colored(f"Cannot convert '{port}' to an integer...", 'red'))
        return

    try:
        sock = s.socket(s.AF_INET, s.SOCK_STREAM)
        address = (host, port)

        # connect_ex() does not raise an exception on the C-level connect call but
        # returns an error code or zero if successful.
        if sock.connect_ex(address) == 0:
            print(colored(f"{port}/tcp is open...", 'green'))
        else:
            print(colored(f"{port}/tcp is closed...", 'red'))

    except KeyboardInterrupt:
        print(colored("You pressed Ctrl-C. Aborting...", 'red'))
        sys.exit()
    except socket.error:
        print(colored("Couldn't connect to server...", 'red'))
        sys.exit()
    finally:
        sock.close()


def port_scanner(host, ports):
    s.setdefaulttimeout(1)
    try:
        ip = ipaddress.ip_address(host)
        host_ip = s.gethostbyname(host)
    except ValueError:
        print(colored(f"Not an IP address. Resovling {host} by name.", 'red'))
        try:
            host_ip = s.gethostbyname(host)
        except:
            print(colored(f"Cannot resolve host {host}", 'red'))
            sys.exit()

    for port in ports:
        threading.Thread(target=connect_port, args=(host, port,),
                daemon=False).start()



def main():
    subprocess.call('clear', shell=True)

    """If you use the word 'Usage' in the initialization string in
    OptionParser(), it will not print out! That is the most bizarre behavior!
    Makes no sense to me..."""
    parser = optparse.OptionParser(f"{sys.argv[0]} -H <host> -p <port(s)>")

    parser.add_option('-H', dest = 'host', type='string', help="Target host IP") 
    parser.add_option('-p', dest='ports', type='string',
            help="Port(s) to be scanned separated by commas") 

    (options, args) = parser.parse_args()
    if options.host == None or options.ports == None:
        print(parser.usage)
        exit(0)

    host = options.host
    ports = options.ports.split(',')

    port_scanner(host=host, ports=ports)

if __name__ == '__main__':
    main()
