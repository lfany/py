#!/usr/bin/env python3

import urllib
import  bs4

file = open('xx.html', 'w+', encoding='utf-8')

def get_content(page):
    # page = 1

    base_url = 'http://www.qiushibaike.com/hot/page/' + str(page)
    print(base_url)
    file.write('<a href="' + base_url + '" />\n')

    req = urllib.request.Request(base_url, data=None, headers={'User-Agent': 'xxx'},
                             method='GET')
    a = urllib.request.urlopen(req)
    html = bs4.BeautifulSoup(a, 'html5lib')


    a = html.findAll('div', attrs={'class': 'content'})

    count = 0
    for i in a:
        count += 1
        print('=================')
        file.write('=================' + '\n')
        print(i.span.text)
        file.write(i.span.text + '\n')
        print('=================')
        file.write('=================' + '\n')
    print(count)
    file.write(str(count) + '\n')


for i in range(10):
    get_content(i + 1)

file.close()