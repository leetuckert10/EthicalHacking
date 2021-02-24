#!/usr/bin/python3

import os
import sys
import crypt
import inspect
import subprocess
from termcolor import colored
from urllib.request import urlopen


"""
Program: mac_changer.py

This simple program uses subprocess and ifconfig to change the mac address. It
seems pretty dumb. It also uses macchanger to change it back before leaveing.

"""

def lineno():
    return inspect.currentframe().f_back.f_lineno


def mod_mac(interface, mac_address):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", mac_address])
    subprocess.call(["ifconfig", interface, "up"])


def main():
    subprocess.call('clear', shell=True)

    interface = input(colored("Enter the interface name: ", 'yellow'))
    mac_address = input(colored("Enter the new mac address: ", 'yellow'))

    before_change = subprocess.check_output(['ifconfig', interface])
    print(before_change.decode('utf-8'))

    mod_mac(interface=interface, mac_address=mac_address)

    after_change = subprocess.check_output(['ifconfig', interface])
    print(after_change.decode('utf-8'))

    subprocess.call(["macchanger", "-p", interface])

if __name__ == "__main__":
    main()
