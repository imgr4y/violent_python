from bluetooth import *

def sdpBrowse(addr):
    services = find_service(address = addr)
    for service in services:
        name = service['name']
        proto = service['protocol']
        port = str(service['port'])
        print '[+] Found ' + str(name) + ' on ' + str(proto) + ':' + port

sdpBrowse('A0:B4:A5:87:A7:6C')