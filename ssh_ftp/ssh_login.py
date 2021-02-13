#!/usr/bin/python3

import os
import sys
import pexpect
import inspect
import subprocess
from termcolor import colored


# PROMPT = '$ '
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
        exit(0)
    elif ret == 1:
        child.sendline("yes")
        ret = child.expect([pexpect.TIMEOUT, '[P|p]assword: '])
        if ret == 0:
            print(colored(f"{lineno()}::spawn process timed out...", 'red'))
            exit(0)
        elif ret == 1:
            child.sendline(pawd)
            ret = child.expect([pexpect.TIMEOUT] + PROMPT)
            if ret == 0:
                print(colored(f"{lineno()}::spawn process timed out...", 'red'))
                exit(0)
            elif ret == 1:
                return child
    elif ret == 2:
        child.sendline(pawd)
        ret = child.expect([pexpect.TIMEOUT] + PROMPT)
        if ret == 0:
            print(colored(f"{lineno()}::spawn process timed out...", 'red'))
            exit(0)
        elif ret == 1:
            return child


def send_command(child, command):
    child.sendline(command)
    child.expect(PROMPT) 
    print(colored(child.before.decode(), 'blue'))


def main():
    subprocess.call('clear', shell=True)

    host = "192.168.1.44"
    user = "msfadmin"
    pawd = "msfadmin"
    cmnd = "cat /etc/shadow | grep -v grep | grep root"

    child = login(host, user, pawd)
    send_command(child, cmnd)



if __name__ == "__main__":
    main()
