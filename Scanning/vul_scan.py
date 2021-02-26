#!/usr/bin/python3

import os
import sys
import subprocess
from termcolor import colored
import socket as sock


def get_banner(ip, port):
    s.setdefaulttimeout(2)
    banner = None
    try:
        s = sock.socket(s.AF_INET, s.SOCK_STREAM)
        address = (ip, port)

        s.connect(address)
        banner = s.recv(1024)
    except s.error as e:
        print(colored(f"{ip}=>{port}:: {e}", 'red'))
    finally:
        s.close()
    return banner


def check_vulnerability(banner, filename):
    with open(filename) as file:
        # data = file.read()
        for line in file.readlines():
            line = line.strip()
            if banner == line:
                print(colored(f"Vulnerability exists for {banner}...", 'green'))
                break


def check_file():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        if not os.path.isfile(filename):
            print(colored(f"{filename} does not exist!", 'red'))
            exit(0)
        if not os.access(filename, os.R_OK):
            print(colored(f"Access denied for {filename}!", 'red'))
            exit(0)
    else:
        print(colored(f"usage: {sys.argv[0]} <filename>", 'red'))
        exit(0)
    return filename



def main():
    subprocess.call('clear', shell=True)

    filename = check_file()
    port_list = [21, 22, 25, 80, 110, 135, 139, 443, 445, 5432]
    host_list = ['192.168.1.10', '192.168.1.44']

    for host in host_list:
        for port in port_list:
            banner = get_banner(host, port)
            if banner:
                # For some reason the telnet port on metasploit throws a
                # UnicodeDecodeError so I had to wrap it in a try block.
                try:
                    banner = banner.decode().strip()
                except UnicodeDecodeError:
                    pass
                print(colored(f"{host} -> {port}/tcp returned: {banner}", 'green'))
                
                check_vulnerability(banner, filename)


if __name__ == "__main__":
    main()
