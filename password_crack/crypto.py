#!/usr/bin/python3

import os
import sys
import crypt
import inspect
import subprocess
from termcolor import colored
from urllib.request import urlopen


"""
Program: crypto.py

"""

def lineno():
    return inspect.currentframe().f_back.f_lineno


def read_user_file(crypto):
    try:
        with open("users.txt", 'r') as file:
            for line in file.readlines():
                line = line.strip()
                (user, password) = line.split(":")
                if password == crypto:
                    return user
    except Execption as e:
        print(colored(f"{e}", 'red'))
        exit(1)

    return None


def read_password_file(pwd_file):
    try:
        with open(pwd_file) as file:
            for password in file.readlines():
                password = password.strip()
                crypto = crypt.crypt(password, password[0:2])
                user = read_user_file(crypto=crypto)
                if user is not None:
                    print(colored(f"Found password '{password}' for user '{user}' in file...",
                            'green'))
                else:
                    print(colored(f"Password '{password}' not found in file...",
                            'red'))

    except Exception as e:
        print(colored(f"{e}", 'red'))


def main():
    subprocess.call('clear', shell=True)

    pwd_file = input(colored("Enter password file name: ", 'yellow'))

    crypt_list = read_password_file(pwd_file=pwd_file)


if __name__ == "__main__":
    main()
