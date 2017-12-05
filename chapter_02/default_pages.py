import ftplib

def returnDefault(ftp):
    try:
        dirList = ftp.nlst()
    except:
        dirList = []
        print '[-] Could not list directory contents.'
        print '[-] Skipping to next target.'
        return

    retList = []

    for filename in dirList:
        fn = fileName.lower()
        if '.php' in fn or '.htm' in fn or '.asp' in fn:
            print '[+] Found default page: ' + filename
            retList.append(fileName)

    return retList

host = '192.168.95.179'
userName = 'guest'
passWord = 'guest'

ftp = ftplib.FTP(host)
ftp.login(userName, passWord)
returnDefault(ftp)