#!/usr/bin/python3

import os
import sys
import hashlib
import inspect
import subprocess
from termcolor import colored
from urllib.request import urlopen


"""Program: md5_pw_crack.py

This program demonstrates how to use a password hash value to search through a
very list of common passwords. The user enters a MD5 hash value and we try and
find that same hash value in the file by converting the passwords there to their
MD5 hash value.

"""

def lineno():
    return inspect.currentframe().f_back.f_lineno


def read_file(hash_str, pwd_file):
    found = False
    try:
        with open(pwd_file) as file:
            for password in file.readlines():
                password = password.strip()
                print(colored(f"Trying {password}", 'yellow'))
                hash_val = hashlib.md5()    # MD5 hash object
                hash_val.update(password.encode('utf-8'))   # update hash object
                if hash_val.hexdigest() == hash_str:
                    print(colored(f"MD5 hash, {hash_str}, is the password, '{password}'",
                            'green'))
                    found = True
                    break
    except Exception as e:
        print(colored(f"{e}", 'red'))

    return found


def main():
    subprocess.call('clear', shell=True)

    hash_str = input(colored("Enter a MD5 hash value: ", 'yellow'))
    pwd_file = input(colored("Enter password file name: ", 'yellow'))

    found = read_file(hash_str=hash_str, pwd_file=pwd_file)

    if not found:
        print(colored(f"MD5 hash, {hash_str}, was not found in the password file",
                'red'))


if __name__ == "__main__":
    main()
