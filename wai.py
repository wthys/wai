# GPLv3

import socket

def check(hostname):
    s = socket.socket()
    try:
        s.bind((hostname, 0))
        return True
    except socket.error, e:
        return False
