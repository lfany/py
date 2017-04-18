#!/usr/bin/env python3
##  pip install beautifulsoup4 bottle html5lib
import urllib.request, urllib.error
import bs4, re
import json
import bottle
import os, sys, atexit, time, _signal


class daemon():
    def __init__(self, pidfile, stdin='/dev/null', stdout='/dev/null', stderr='/dev/null'):
        self.stdin = stdin
        self.stdout = stdout
        self.stderr = stderr
        self.pidfile = pidfile

    def daemonize(self):
        # 第一次fork，生成子进程，脱离父进程
        try:
            pid = os.fork()
            if pid > 0:
                sys.exit(0)
        except OSError as e:
            sys.stderr.write("fork fist faild:%d (%s)\n" % (e.errno, e.strerror))
            sys.exit(1)

        # 修改工作目录
        os.chdir('/')
        # 设置新的会话连接
        os.setsid()
        # 重新设置文件创建权限
        os.umask(0)

        # 第二次fork，禁止进程打开终端
        try:
            pid = os.fork()
            if pid > 0:
                sys.exit(0)
        except OSError as e:
            sys.stderr.write("fork second faild:%d (%s)\n" % (e.errno, e.strerror))
            sys.exit(1)

        sys.stdout.flush()
        sys.stderr.flush()

        # 重定向标准输入、输出
        si = open(self.stdin, 'r')
        so = open(self.stdout, 'a+')
        se = open(self.stderr, 'a+')
        os.dup2(si.fileno(), sys.stdin.fileno())
        os.dup2(so.fileno(), sys.stdout.fileno())
        os.dup2(se.fileno(), sys.stderr.fileno())

        # 注册退出函数
        atexit.register(self.delpid)
        pid = str(os.getpid())
        open(self.pidfile, 'w+').write("%s\n" % pid)

    def delpid(self):
        os.remove(self.pidfile)

    def start(self):
        try:
            pf = open(self.pidfile, 'r')
            pid = int(pf.read().strip())
            pf.close()
        except IOError:
            pid = None

        if pid:
            ms = "pidfile %s already exist,daemon already running\n"
            sys.stderr.write(ms % self.pidfile)
            sys.exit(1)

        self.daemonize()
        self.run()

    def stop(self):
        try:
            pf = open(self.pidfile, 'r')
            pid = int(pf.read().strip())
            pf.close()
        except IOError:
            pid = None

        if not pid:
            ms = "pidfile %s does not exit,daemon not running\n"
            sys.stderr.write(ms % self.pidfile)
            return

        try:
            while 1:
                os.kill(pid, _signal.SIGTERM)
                time.sleep(0.1)
                os.remove(self.pidfile)
        except OSError as err:
            err = str(err)
            if err.find('No sush process') > 0:
                if os.path.exists(self.pidfile):
                    os.remove(self.pidfile)
                else:
                    print
                    str(err)
                    sys.exit(1)

    def restart(self):
        self.stop()
        self.start()

    # 该方法用于在子类中重新定义，用来运行你的程序
    def run(self):
        """ run your fun"""


###以上代码可以做成一个库文件，也可以放在一个文件中###
###以下代码可以引用上面的库文件#########
class mydaemon(daemon):
    # 重新定义run函数，以运行你的功能
    def run(self):
        @bottle.route('/qiushi/<page>')
        def qiushi(page):
            return get_page(page)

        bottle.run(host='localhost', port=3333)


class Data:
    def __init__(self, lists, page) -> None:
        super().__init__()
        self.lists = lists
        self.page = page
        self.errorcode = 0
        self.msg = ''


class Article:
    def __init__(self, article, url, vote, comment, author):
        super().__init__()
        self.article = article
        slef.url = url
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
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'}


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
                item.findAll('a', class_='contentHerf')[0].attrs['href'],
                item.findAll('span', class_='stats-vote')[0].i.text,
                item.findAll('span', class_='stats-comments')[0].i.text,
                author
            )
            lists.append(article)
        data = json.dumps(Data(lists, page), default=lambda o: o.__dict__, sort_keys=True, indent=4,
                          ensure_ascii=False)
        # print(data)
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


if __name__ == '__main__':
    daemon = mydaemon('/tmp/pidfile', stdout='/tmp/result')
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            daemon.start()
        elif 'stop' == sys.argv[1]:
            daemon.stop()
        elif 'restart' == sys.argv[1]:
            daemon.restart()
        else:
            print('unkonow command')
            sys.exit(2)
        sys.exit(0)
    else:
        print("usage:%s start/stop/restart" % sys.argv[0])
        sys.exit(2)
