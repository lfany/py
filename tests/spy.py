#!/usr/bin/env python3

import urllib
import  bs4
import requests

file = open('xx.html', 'w+', encoding='utf-8')

def get_content(page):
    # page = 1

    base_url = 'http://www.qiushibaike.com/hot/page/' + str(page)
    print(base_url)
    file.write('<a href="' + base_url + '" > ' + base_url + ' </a><br />\n')

    # req = urllib.request.Request(base_url, data=None, headers={'User-Agent': 'xxx'},
    #                          method='GET')
    # a = urllib.request.urlopen(req)
    a = requests.get(base_url, headers={'User-Agent': 'xxx'})
    html = bs4.BeautifulSoup(a.text, 'html5lib')


    a = html.findAll('div', attrs={'class': 'article block untagged mb15'})

    count = 0
    for i in a:
        count += 1
        print('=================')
        file.write('=================' + '<br />\n')
        print(i.h2.text)
        file.write(i.h2.text + '<br />\n')
        print(i.span.text)
        file.write(i.span.text + '<br />\n')
        print('=================')
        file.write('=================' + '<br />\n')
    print(count)
    file.write(str(count) + '<br />\n')


for i in range(10):
    get_content(i + 1)

file.close()