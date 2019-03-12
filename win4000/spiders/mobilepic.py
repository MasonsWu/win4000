# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from win4000.items import MobileNewItem
from urllib.parse import urljoin
from scrapy.loader import ItemLoader
import re


class MobilepicSpider(scrapy.Spider):
    name = 'mobilepic'
    allowed_domains = ['win4000.com']
    start_urls = []
    for page in range(1,6):
        page = "http://www.win4000.com/mobile_0_0_0_{0}.html".format(page)
        start_urls.append(page)

    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }

    def parse(self, response):
        pic_nodes = response.xpath("//*/div[@class='Left_bar']/div[1]/div/div/div/ul/li/a")
        for pic_urls in pic_nodes:
            pic_url = pic_urls.xpath(".//@href").extract_first()
            yield Request(url=urljoin(response.url,pic_url),headers=self.headers,callback=self.mobile_detail)


    def mobile_detail(self,response):
        # item = MobileNewItem()
        # titles = response.xpath(".//*[@id='scroll']/li/a/img/@title").extract()
        # for title in titles:
        #     item['pic_title'] = title
        # item['pic_size'] = response.xpath("//*/div[@class='Bigimg_style']/span[@class='size']/em/text()").extract()
        # pics = response.xpath(".//*[@id='scroll']/li/a/img/@data-original").extract()
        # for pic in pics:
        #     item['pic_urls'] = [pic]
        # item['pic_time'] = response.xpath(".//div[@class='Bigimg_style']/span[@class='time']/text()").extract()
        # return item
        """
        以上写法正确，但是爬取的图片不完整，提取的是图片的缩略图
        """
        image_urls = response.xpath(".//*[@id='scroll']/li/a/@href").extract()
        for image_url in image_urls:
            pic_url = image_url
            yield Request(url=pic_url,headers=self.headers,callback=self.mobile_pic_content)


    def mobile_pic_content(self,response):
        item = MobileNewItem()
        # item_loader = ItemLoader(item=MobileNewItem,response=response)
        # item_loader.add_xpath("pic_title","//*/div[@class='Bigimg']/div[@class='ptitle']/h1/text() | //*/div[@class='Bigimg']/div[@class='ptitle']/span/text()")
        # item_loader.add_xpath("pic_size","//*/div[@class='Bigimg_style']/span[@class='size']/em/text()")
        # item_loader.add_xpath("pic_urls",".//*[@id='pic-meinv']/a/img/@src")
        # item_loader.add_xpath("pic_time","//*/div[@class='Bigimg_style']/span[@class='time']/text()")
        # image_item = item_loader.load_item()
        # return image_item
        item['pic_title'] = response.xpath("//*/div[@class='Bigimg']/div[@class='ptitle']/h1/text()").extract()
        item['pic_size'] = response.xpath("//*/div[@class='Bigimg_style']/span[@class='size']/em/text()").extract()
        item['pic_urls'] = response.xpath(".//*[@id='pic-meinv']/a/img/@src").extract()
        item['pic_time'] = response.xpath("//*/div[@class='Bigimg_style']/span[@class='time']/text()").extract()
        return item









