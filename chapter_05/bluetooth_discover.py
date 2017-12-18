import time
from bluetooth import *
from datetime import datetime

alreadyFound = []

def findDevs():
    foundDevs = discover_devices(lookup_names=True)
        
    for (addr, name) in foundDevs:
        if addr not in alreadyFound:
            print '[*] Found Bluetooth device: ' + str(name)
            print '[+] MAC address: ' + str(addr)
            print '[+] Time is: ' + str(datetime.now())
            alreadyFound.append(addr)

while True:
    findDevs()
    time.sleep(5)