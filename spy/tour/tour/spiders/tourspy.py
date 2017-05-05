# -*- coding: utf-8 -*-
import scrapy


class TourspySpider(scrapy.Spider):
    name = "tourspy"
    allowed_domains = ["www.baidu.com"]
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        pass
