import PyPDF2
import optparse
from PyPDF2 import PdfFileReader

def printMeta(fileName):
    pdfFile = PdfFileReader(open(fileName, 'rb'))
    docInfo = pdfFile.getDocumentInfo()
    
    print '[*] PDF metadata for: ' + str(fileName)
    for metaItem in docInfo:
        print '[+] ' + metaItem + ':' + docInfo[metaItem]

def main():
    parser = optparse.OptionParser('usage %prog ' + '-F <PDF file name>')
    parser.add_option('-F', dest='fileName', type='string', help='specify PDF file name')
    (options, args) = parser.parse_args()

    fileName = options.fileName

    if fileName == None:
        print parser.usage
        exit(0)
    else:
        printMeta(fileName)

if __name__ == '__main__':
    main()