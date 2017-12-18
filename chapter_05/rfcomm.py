from bluetooth import *

def rfcommCon(addr, port):
    sock = BluetoothSocket(RFCOMM)
    try:
        sock.connect((addr, port))
        print '[+] RFCOMM Port ' + str(port) + ' open'
        sock.close()

    except Exception, e:
        print '[-] RFCOMM Port ' + str(port) + ' closed'

for port in range(1, 30):
    rfcommCon('A0:B4:A5:87:A7:6C', port)