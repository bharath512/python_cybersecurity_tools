#!/usr/bin/python

import netfilterqueue
import scapy.all as scapy

def process_packet(packet):
    scapy_packets = scapy.IP(packet.get_payload())
    if scapy_packets.haslayer(scapy.Raw):
        if scapy_packets[scapy.TCP].dport == 80:
            print ("HTTP request")
            if b".exe" in scapy_packets[scapy.Raw].load:
                print (scapy_packets.show())
        elif scapy_packets[scapy.TCP].sport == 80:
            print ("HTTP response")
            print (scapy_packets.show())

    packet.accept()

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()
