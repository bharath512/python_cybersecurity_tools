import subprocess

interface=input("Interface > ")
mac_address=input("New MAC address > ")

print("[+] Changing MAC address of "+interface+" to "+mac_address+"\n")
subprocess.call(["ifconfig",interface,"down"])
subprocess.call(["ifconfig",interface,"hw","ether",mac_address])
subprocess.call(["ifconfig",interface,"up"])
subprocess.call(["ifconfig",interface])
print("\n[+] Changed MAC address of "+interface+" to "+mac_address)