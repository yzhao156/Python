import urllib.request
import os
import random

def get_page(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36')

    proxies = ['119.6.114.70:81', '111.1.36.9:80', '203.144.162:8080']
    proxy = random.choice(proxies)

    proxy_support = urllib.request.ProxyHandler({'http':proxy})
    opener = urllib.request.build_opener(proxy_support)
    urllib.request.install_opener(opener)

    response = urllib.request.urlopen(url)
    html = response.read().decode('utf-8')
    print(html)

    a = html.find('current-comment-page') + 23
    b = html.find(']', a)

    print(html[a:b])

def find_imgs(url):
    pass

def save_imgs(folder, img_addrs):
    pass

def download_mm(folder = 'OOXX', pages = 10):
    os.mkdir(folder)
    os.chdir(folder)

    url = "http://jandan.net/ooxx/"
    page_num = int(get_page(url))

    for i in range(pages):
        page_num -= 1
        page_url = url + 'page-' + str(page_num) + '#comments'
        img_addrs = find_imgs(page_url)
        save_imgs(foolder, img_addrs)

if __name__ == '__main__':
    download_mm()
