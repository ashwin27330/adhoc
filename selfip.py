#!/usr/bin/python

import socket


def get_Host_name_IP():
        try:
                host_name = socket.gethostname()
                host_ip = socket.gethostbyname(host_name)
                print("Hostname : ",host_name)
                print("IP : ",host_ip)

        except:
                print("Unable to gt hostname and IP")

get_Host_name_IP()









