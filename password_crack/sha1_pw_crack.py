#!/usr/bin/python3

import os
import sys
import hashlib
import inspect
import subprocess
from termcolor import colored
from urllib.request import urlopen


"""Program: sha1_pw_crack.py

This program demstrates how to use a password hash value to search through a
very large list of common passwords, converting thime to SHA! and checking if
the hash value you entered is found. There is some very good stuff in here.

"""

def lineno():
    return inspect.currentframe().f_back.f_lineno


def main():
    subprocess.call('clear', shell=True)

    hash_str = input(colored("Enter a SHA1 hash value: ", 'yellow'))
    pwd_list = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt').read(), 'utf-8')

    found = False
    for pwd in pwd_list.split():
        hash_val = hashlib.sha1()
        hash_val.update(pwd.encode())
        if hash_val.hexdigest() == hash_str:
            print(colored(f"SHA1 hash, {hash_str}, is the password, '{pwd}'", 'green'))
            found = True
            break

    if not found:
        print(colored(f"SHA1 hash, {hash_str}, was not found in the password file",
                'red'))


if __name__ == "__main__":
    main()
