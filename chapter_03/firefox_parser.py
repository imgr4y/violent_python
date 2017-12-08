import sqlite3
import optparse
import re
import os

def printGoogle(placesDB):
    conn = sqlite3.connect(placesDB)
    c = conn.cursor()

    c.execute('SELECT url, datetime(visit_date/1000000, \'unixepoch\') FROM moz_places, moz_historyvisits WHERE visit_count > 0 AND moz_places.id == moz_historyvisits.place_id;')

    print '\n[*] -- Found Google Results --'

    for row in c:
        url = str(row[0])
        date = str(row[1])
        if 'google' in url.lower():
            r = re.findall(r'q=.*\&', url)

            if r:
                search = r[0].split('&')[0]
                search = search.replace('q=', '').replace('+', ' ')
                print '[+] ' + date + ' - Searched for: ' + search

def printDownloads(downloadDB):
    conn = sqlite3.connect(downloadDB)
    c = conn.cursor()

    c.execute('SELECT name, source, datetime(endTime/1000000, \'unixepoch\') FROM moz_downloads;')

    print '\n[*] -- Files downloaded --'
    for row in c:
        print '[+] File: ' + str(row[0]) + ' from source: ' + str(row[1]) + ' at: ' + str(row[2])

def printCookies(cookiesDB):
    try:
        conn = sqlite3.connect(cookiesDB)
        c = conn.cursor()

        c.execute('SELECT host, name, value FROM moz_cookies;')
        print '\n[*] -- Found cookies --'
        
        for row in c:
            host = str(row[0])
            name = str(row[1])
            value = str(row[2])

            print '[+] Host: ' + host + ', Cookie: ' + name + ', Value: ' + value

    except Exception, e:
        if 'encrypted' in str(e):
            print '\n[*] Error reading your cookies database.'
            print '[*] Upgrade your python sql3 library.'
            exit(0)

def printHistory(placesDB):
    try:
        conn = sqlite3.connect(placesDB)
        c = conn.cursor()

        c.execute('SELECT url, datetime(visit_date/1000000, \'unixepoch\') FROM moz_places, moze_historyvisits WHERE visit_count > 0 and moz_places.id == moz_historyvisits.place_id;')

        print '\n[*] -- Found history --'

        for row in c:
            url = str(row[0])
            date = str(row[1])
            print '[+] ' + date + ' - Visited: ' + url
    except Exception, e:
        if 'encrypted' in str(e):
            print '[*] Error reading your places database.'
            print '[*] Upgrade your Python sql3 library.'
            exit(0)

def main():
    parser = optparse.OptionsParser("usage%prog -p <firefox profile path>")
    parser.add_option('-p', dest='pathName', type='string', help='specify a firefox profile path')
    (options, args) = parser.parse_args()
    pathName = options.pathName

    if pathName == None:
        print parser.usage
        exit(0)
    elif os.path.isdir(pathName) == False:
        print '[!] Path does not exist: ' + pathName
        exit(0)
    else:
        downloadDB = os.path.join(pathName, 'downloads.sqlite')
        if os.path.isfile(downloadDB):
            printDownloads(downloadDB)
        else:
            print '[!] Downloads db does not exist: ' + downloadDB
        
        cookiesDB = os.path.join(pathName, 'cookies.sqlite')
        if os.path.isfile(cookiesDB):
            printCookies(cookiesDB)
        else:
            print '[!] Cookies db does not exist: ' + cookiesDB

        placesDB = os.path.join(pathName, 'places.sqlite')
        if os.path.isfile(placesDB):
            printHistory(placesDB)
            printGoogle(placesDB)
        else:
            print '[!] Places db does not exist: ' + placesDB
            
if __name__ == '__main__':
    main()