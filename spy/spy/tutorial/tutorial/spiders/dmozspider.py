# -*- coding: utf-8 -*-
import scrapy


class DmozSpiderSpider(scrapy.Spider):
    name = "dmozspider"
    allowed_domains = ["dmoztools.net"]
    start_urls = [
        "http://dmoztools.net/Computers/Programming/Languages/Python/Books/",
        "http://dmoztools.net/Computers/Programming/Languages/Python/Resources/"
    ]

    def parse(self, response):
        # filename = response.url.split("/")[-2] + '.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        for sel in response.xpath('//*[@id="site-list-content"]'):
            from spy.spy.tutorial.tutorial.items import TutorialItem
            item = TutorialItem()
            # print(sel.extract())
            item['title'] = sel.xpath('//div[@class="site-title"]/text()').extract()
            item['link'] = sel.xpath('//div[@class="title-and-desc"]/a/@href').extract()
            item['desc'] = sel.xpath('//div[@class="site-descr "]/text()').extract()
            for i in item['link']:
                j = item['link'].index(i)
                item['link'][j] = response.url + i
                yield {
                    'title': item['title'][j],
                    'link': item['link'][j],
                    'desc': item['desc'][j],
                }
