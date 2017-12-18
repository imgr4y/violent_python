from scapy.all import *

interface = 'wlp4s0'
probeReqs = []

def sniffProbe(p):
    if p.haslayer(Dot11ProbeReq):
        netName = p.getlayer(Dot11ProbeReq).info
        if netName not in probeReqs:
            probeReqs.append(netName)
            print '[+] Detected new probe request: ' + netName

sniff(iface=interface, prn=sniffProbe)