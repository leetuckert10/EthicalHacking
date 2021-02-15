#!/usr/bin/python3

import os
import sys
import inspect
import subprocess
import ftplib
from termcolor import colored


"""Program: ftp_login.py"""

def lineno():
    return inspect.currentframe().f_back.f_lineno


def login(host):
    try:
        ftp = ftplib.FTP(host, timeout=5)
        ftp.login('anonymous', 'anonymous')
        print(colored(f"Anonymous login to {host} successful!", 'green'))
        ftp.quit
    except ftplib.all_errors as e:
        print(colored(f"{e}", 'red'))


def main():
    subprocess.call('clear', shell=True)

    host = input(colored("Enter the host IP address: ", 'yellow'))
    login(host)


if __name__ == "__main__":
    main()
