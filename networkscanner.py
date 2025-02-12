#! /usr/bin/python
import optparse
import scapy.all as scapy

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-t","--target",dest="ip",help="Enter the IP wants to search")
    (options, arugumets) = parser.parse_args()
    if not (options.ip):
        parser.error("Please enter IP to search. Use --help for more info")
    return options

def scan(ip):
    arp_request=scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    client_list=[]
    for element in answered_list:
        client_dict={"ip":element[1].psrc,"Mac":element[1].hwsrc}
        client_list.append(client_dict)
    return (client_list)

def print_result(result_list):
    print("IP\t\t\tMAC Address\n-------------------------------------------")
    for client in result_list:
        print(client["ip"]+"\t\t"+client["Mac"])

(options) = get_arguments()
scan_result = scan(options.ip)
print_result(scan_result)
