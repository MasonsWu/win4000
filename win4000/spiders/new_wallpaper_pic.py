# -*- coding: utf-8 -*-
import scrapy


class NewWallpaperPicSpider(scrapy.Spider):
    name = 'new_wallpaper_pic'
    allowed_domains = ['win4000.com']
    start_urls = ['http://win4000.com/']

    def parse(self, response):
        pass
