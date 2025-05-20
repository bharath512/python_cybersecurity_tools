import subprocess

interface=input("Interface > ")
mac_address=input("New MAC address > ")

subprocess.call(["ifconfig",interface,"down"])
subprocess.call(["ifconfig",interface,"hw","ether",mac_address])
subprocess.call(["ifconfig",interface,"up"])
