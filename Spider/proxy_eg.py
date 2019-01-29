import urllib.request
import random
url = 'https://whatismyipaddress.com'

iplist = ['193.203.208.166', '111.1.32.28', '183.203.208.166']

proxy_support = urllib.request.ProxyHandler({'http':random.choice(iplist)})#'165.227.53.107'})

opener = urllib.request.build_opener(proxy_support)
opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36')]

urllib.request.install_opener(opener)

response = urllib.request.urlopen(url)
html = response.read().decode('utf-8')

print(html)