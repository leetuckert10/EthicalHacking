#!/usr/bin/python3

import os
import sys
import crypt
import inspect
import subprocess
from termcolor import colored
from urllib.request import urlopen


"""Program: gen_crypt_passwords.py

This program is just a utility program for writing a users file that has user
names and encrypted passwords separated by a ":". The program cryptic.py needs
"users.txt". Has usage of the crypt library and examplies fo reading and writing
files in Python.

"""

""" Just a list of made up users without encrypted passwords."""
users = {"admin": "",
         "john": "",
         "carly": "",
         "lee": "",
         "root": "",
         "joe": "",
         "angus": "",
         "bill": "",
         "mama": "",
}

def lineno():
    return inspect.currentframe().f_back.f_lineno


def update_users(crypt_list):
    for user in users.keys():
        users[user] = crypt_list.pop()
        print(colored(f"{user}:{users[user]}", 'yellow'))


def write_password_file():
    try:
        with open("users.txt", 'w') as file:
            for (user, password) in users.items():
                file.write(f"{user}:{password}\n")
    except Execption as e:
        print(colored(f"{e}", 'red'))


def read_password_file(pwd_file):
    crypt_list = []
    try:
        with open(pwd_file) as file:
            for password in file.readlines():
                password = password.strip()
                crypt_list.append(crypt.crypt(password, password[0:2]))
    except Exception as e:
        print(colored(f"{e}", 'red'))

    update_users(crypt_list=crypt_list)


def main():
    subprocess.call('clear', shell=True)

    pwd_file = input(colored("Enter password file name: ", 'yellow'))

    read_password_file(pwd_file=pwd_file)
    write_password_file()


if __name__ == "__main__":
    main()
