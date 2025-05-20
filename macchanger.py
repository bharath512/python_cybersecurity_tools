#!/usr/bin/env python

import subprocess
import optparse
import re

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

def get_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface]).decode('ascii')
    mac_output_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    if mac_output_result:
        return mac_output_result.group(0)
    else:
        print("No MAC found, Check your interface input")

def change_mac(interface, new_mac):
    print("[+] Changing MAC address of " + interface + " to " + new_mac + "\n")
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

options = get_argument()
current_mac = str(get_mac(options.interface))
print("Current MAC address: "+current_mac)

change_mac(options.interface, options.new_mac)

current_mac = str(get_mac(options.interface))
if current_mac == options.new_mac:
    print("[+] MAC Address of " + options.interface+ " changed to " + current_mac)
else:
    print("[+] MAC address not changed")

