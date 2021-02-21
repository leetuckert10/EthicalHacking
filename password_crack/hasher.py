#!/usr/bin/python3

import os
import sys
import ftplib
import hashlib
import inspect
import subprocess
from termcolor import colored


"""Program: hasher.py

Demonstrates create various types of hash values from a string entered at the
keyboard.
"""

def lineno():
    return inspect.currentframe().f_back.f_lineno


def main():
    subprocess.call('clear', shell=True)

    hash_str = input(colored("Enter a string to hash: ", 'yellow'))
    hash_md5 = hashlib.md5()
    hash_md5.update(hash_str.encode())
    print(colored(f"MD5 of {hash_str}: {hash_md5.hexdigest()}", 'blue'))

    hash_sha1 = hashlib.sha1()
    hash_sha1.update(hash_str.encode())
    print(colored(f"SHA1 of {hash_str}: {hash_sha1.hexdigest()}", 'blue'))

    hash_sha224 = hashlib.sha224()
    hash_sha224.update(hash_str.encode())
    print(colored(f"SHA224 of {hash_str}: {hash_sha224.hexdigest()}", 'blue'))

    hash_sha256 = hashlib.sha256()
    hash_sha256.update(hash_str.encode())
    print(colored(f"SHA256 of {hash_str}: {hash_sha256.hexdigest()}", 'blue'))

    hash_sha512 = hashlib.sha512()
    hash_sha512.update(hash_str.encode())
    print(colored(f"SHA512 of {hash_str}: {hash_sha512.hexdigest()}", 'blue'))


if __name__ == "__main__":
    main()
