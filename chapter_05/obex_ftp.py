import obexftp

try:
    btPrinter = obexftp.client(obexftp.BLUETOOTH)
    btPrinter.connect('A0:B4:A5:87:A7:6C', 2)
    btPrinter.put_file('/test.jpg')
    print '[+] Printed test image.'
except:
    print '[-] Failed to print test image.'