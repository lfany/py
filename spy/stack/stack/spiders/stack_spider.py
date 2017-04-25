# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector


class StackSpiderSpider(scrapy.Spider):
    name = "stack_spider"
    allowed_domains = ["stackoverflow.com"]
    start_urls = ['http://stackoverflow.com/questions?pagesize=50&sort=newest']

    def parse(self, response):
        questions = Selector(response).xpath('//div[@class="summary"]/h3')

        for question in questions:
            import sys
            sys.path.extend(['E:\\py', 'E:/py'])
            from spy.stack.stack.items import StackItem
            item = StackItem()
            item['title'] = question.xpath(
                'a[@class="question-hyperlink"]/text()').extract()[0]
            item['url'] = question.xpath(
                'a[@class="question-hyperlink"]/@href').extract()[0]
            yield item
        pass
