#!/usr/bin/env python

import scapy.all as scapy

def scan(ip):
    scapy.arping(ip)

scan("192.168.221.2/24")




#########################################################################################
# Note
# scapy.arping() module will not work with python2 version. It will get frozen
#########################################################################################