# -*- coding: utf-8 -*-
import scrapy


class BeautypicSpider(scrapy.Spider):
    name = 'beautypic'
    allowed_domains = ['win4000.com']
    start_urls = ['http://win4000.com/']

    def parse(self, response):
        pass
