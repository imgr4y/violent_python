from scapy.all import *

def pktPrint(pkt):
    if pkt.haslayer(Dot11Beacon):
        print '[+] Detected 802.11 beacon frame.'
    elif pkt.haslayer(Dot11ProbeReq):
        print '[+] Detected 802.11 probe request frame.'
    elif pkt.haslayer(TCP):
        print '[+] Detected a TCP packet.'
    elif pkt.haslayer(DNS):
        print '[+] Detected a DNS packet.'

conf.iface = 'mon0'
sniff(prn=pktPrint)
