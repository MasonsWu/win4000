# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


from scrapy.http import Request
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem


import pymysql,MySQLdb

class Win4000Pipeline(object):
    def process_item(self, item, spider):
        return item


class SaveImagesWin4000Pipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for images_url in item['pic_urls']:
            return Request(images_url)

    def item_completed(self, results, item, info):
        image_path = [x['path'] for ok,x in results if ok]
        if not image_path:
            raise DropItem("Item contains no images !s")
        item['pic_path'] = image_path
        return item


class SaveMysqlPipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect('127.0.0.1','root','','win4000',charset='utf8')
        self.cur = self.conn.cursor()

    def process_item(self,item,spider):
        insert_sql = """insert into infos (pic_title,pic_size,pic_urls,pic_time) VALUES (%s,%s,%s,%s)"""
        self.cur.execute(insert_sql,(item['pic_title'],item['pic_size'],item['pic_urls'],item['pic_time'] ))
        self.conn.commit()
        return item




