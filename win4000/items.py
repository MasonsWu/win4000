# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose,TakeFirst,Join


class Win4000Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


def add_title(value):
    return value + "QQ: 2457179751"

class MobileNewItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pic_title = scrapy.Field()
    pic_size = scrapy.Field()
    pic_urls = scrapy.Field()
    pic_path = scrapy.Field()
    pic_time = scrapy.Field()