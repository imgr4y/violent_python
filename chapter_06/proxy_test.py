import mechanize

def testProxy(url, proxy):
    browser = mechanize.Browser()
    browser.set_proxies(proxy)
    page = browser.open(url)
    source_code = page.read()
    print source_code

url = 'http://syngress.com/'
hideMeProxy = {'http': '47.89.241.103:8080'}
testProxy(url, hideMeProxy)