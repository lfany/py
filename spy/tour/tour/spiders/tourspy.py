# -*- coding: utf-8 -*-
import scrapy


class TourspySpider(scrapy.Spider):
    name = "tourspy"
    params = 's?wd='
    keyword = '你好'
    allowed_domains = ["www.baidu.com"]
    start_urls = ['http://www.baidu.com/' + params + keyword]

    def parse(self, response):
        # self.logger.info("%s received", response.url)
        # print(response.body.decode('utf-8'))
        for i in response.xpath('//div[@class="result c-container "]'):
            print(i.xpath('h3/a/@href').extract_first())
            words = i.xpath('h3/a/text()').extract()
            words.insert(1, i.xpath('h3/a/em/text()').extract_first())
            print('##'.join(words))

            from spy.tour.tour.items import TourItem
            item = TourItem()
            item['title'] = '##'.join(words).encode('utf-8').decode('unicode_escape')
            item['url'] = i.xpath('h3/a/@href').extract_first()
            yield item  # {
            #     'title': '##'.join(words),
            #     'url': i.xpath('h3/a/@href').extract_first(),
            # }

            # i.xpath('h3/a/em/text()').extract_first(),
            # i.xpath('h3/a/text()').extract())
            # print(i.xpath('h3/a').extract_first())
