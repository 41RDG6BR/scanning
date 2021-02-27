#!/usr/bin/python3
from termcolor import colored
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.setdefaulttimeout(1)

host = "192.168.0.2"

def portscanner(port):
        if sock.connect_ex((host, port)):
            print (colored("[!!] Port %d is closed" % (port), 'red'))
        else:
            print (colored("[+] Port %d is opened" % (port), 'green'))

for port in range(1,4000):
    portscanner(port)    