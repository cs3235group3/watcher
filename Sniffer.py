from scapy.all import *
import threading

class Sniffer(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        print('Sniffer initiated')

    def run(self):
        self.sniff()

    def sniff(self):
        sniff(prn=self.packet_callback, filter="arp", store=0)

    def packet_callback(self, packet):
        if packet[ARP].op == 1:
            response = 'Request: ' + packet[ARP].psrc + ' is asking about ' + packet[ARP].pdst
        elif packet[ARP].op == 2:
            response = 'Response: ' + packet[ARP].hwsrc + ' has address ' + packet[ARP].psrc
        print(response)