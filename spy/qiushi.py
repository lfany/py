#!/usr/bin/env python3
##  pip install beautifulsoup4 bottle html5lib
import urllib.request, urllib.error
import bs4, re
import json
import bottle


class Data:
    def __init__(self, lists) -> None:
        super().__init__()
        self.lists = lists
        self.errorcode = 0
        self.msg = ''


class Article:
    def __init__(self, article, vote, comment, author):
        super().__init__()
        self.article = article
        self.vote = vote
        self.comment = comment
        self.author = author


class Author:
    def __init__(self, name, age, sex, png, page):
        super().__init__()
        self.name = name
        self.age = age
        self.sex = sex
        self.png = png
        self.page = page


schema = 'http:'
base_url = 'http://www.qiushibaike.com'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'}


def get_page(page):
    url = 'http://www.qiushibaike.com/hot/page/' + str(page)
    request = urllib.request.Request(url, headers=headers)
    print(request.full_url)

    try:
        response = urllib.request.urlopen(request)
        content = response.read()
        soup = bs4.BeautifulSoup(content, 'html5lib')
        lists = []
        items = soup.findAll('div', class_='article block untagged mb15', id=re.compile('qiushi_tag_\d+'))
        for item in items:
            # print('=============================')
            authors = item.findAll('div', class_='author clearfix')

            # authorName,
            # authorAge,
            # authorSex,
            # authorPng,
            # authorPage

            for i in authors:
                # print(i.img.attrs['alt'])
                # print(schema + i.img.attrs['src'])
                # print(base_url + i.a.attrs['href'])
                # print(i.div.text)
                # print(i.div.attrs['class'])
                if 'womenIcon' in i.div.attrs['class']:  # woman
                    sex = 'woman'
                else:
                    sex = 'man'
                    # print(i.a)
                authorName = i.img.attrs['alt']
                authorAge = i.div.text
                authorSex = sex
                authorPng = schema + i.img.attrs['src']
                authorPage = base_url + i.a.attrs['href']
                author = Author(authorName, authorAge, authorSex, authorPng, authorPage)

            # print(item.span.text)
            # print(item.findAll('span', class_='stats-vote')[0].i.text)  # vote
            # print(item.findAll('span', class_='stats-comments')[0].i.text)  # comment
            # print('=============================')

            article = Article(
                item.span.text,
                item.findAll('span', class_='stats-vote')[0].i.text,
                item.findAll('span', class_='stats-comments')[0].i.text,
                author
            )
            lists.append(article)
        data = json.dumps(Data(lists), default=lambda o: o.__dict__, sort_keys=True, indent=4,
                          ensure_ascii=False)
        print(data)
        return data
        # dumps = json.dumps(article, default=lambda o: o.__dict__, sort_keys=True, indent=4)
        # print(dumps)

    except urllib.error.URLError as e:
        if hasattr(e, 'reason'):
            print(e.reason)
        return ''
    except TimeoutError as e:
        if hasattr(e, 'reason'):
            print(e.reason)
        else:
            print(e)
        return ''
    except AttributeError as e:
        print('AttributeError')
        return ''

        # article = Article(None, None, None, None, None, None, None, None)


@bottle.route('/qiushi/<page>')
def qiushi(page):
    return get_page(page)


bottle.run(host='localhost', port=3333)
