#!/usr/bin/env python

import subprocess
import optparse

def change_mac(interface, new_mac):
    print("[+] Changing MAC address of " + interface + " to " + new_mac + "\n")
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])
    subprocess.call(["ifconfig", interface])
    print("\n[+] Changed MAC address of " + interface + " to " + new_mac)

parser = optparse.OptionParser()

parser.add_option("-i","--interface",dest="interface",help="Interface name to change MAC address")
parser.add_option("-m","--mac",dest="new_mac",help="New MAC address")

(options, arguments) = parser.parse_args()

change_mac(options.interface, options.new_mac)