#!/usr/bin/env python

import subprocess
import optparse

def get_argument():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface name to change MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("Please enter interface, use --help for more info")
    elif not options.new_mac:
        parser.error("Please enter new MAC, use --help for more info")
    return options

def change_mac(interface, new_mac):
    print("[+] Changing MAC address of " + interface + " to " + new_mac + "\n")
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])
    subprocess.call(["ifconfig", interface])
    print("\n[+] Changed MAC address of " + interface + " to " + new_mac)

options = get_argument()
change_mac(options.interface, options.new_mac)