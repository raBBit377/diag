#!/bin/python

#скріпт діагностики

import socket
import re, uuid
import urllib.request
import subprocess
from color import colors

#ping 
def ping(ip_address):
    ping_command = f"ping -c 400 {ip_address}"
    subprocess.call(ping_command, shell=True)

#mac + ip-add
def get_ip():
    host_name = socket.gethostname()
    IP_local = socket.gethostbyname(host_name)
    IP_global = urllib.request.urlopen('https://ident.me').read().decode('utf8')
    return host_name, IP_local, IP_global

if __name__ == '__main__':


    #menu
    print("Please select operation :\n" \
            "1. - ping\n" \
            "2. - ip (local, global,mac address)\n" )

    try:
        select = int(input("Select operations form 1, 2 :"))
    
    except ValueError:
        print('не число')
    else:

        if select == 1:
            ip = input('write your ip address:')
            if not ip:
                ip = '8.8.8.8'
            print(ping(ip))

        if select == 2:
            host_name, IP_local, IP_global = get_ip()

            print("Host Name is --> " + colors.fg.green + host_name + colors.reset )
            print("Computer IP Address (local) --> " + colors.fg.green + IP_local + colors.reset)
            print("Computer IP Address (global) --> " + colors.fg.green + IP_global + colors.reset)
            # MAC address
            print("Computer MAC address --> " + colors.fg.green, end="")
            print(':'.join(re.findall('..', '%012x' %uuid.getnode()))+ colors.reset)
            
          
                    