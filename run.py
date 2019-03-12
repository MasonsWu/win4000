#  _*_ coding:utf-8 _*_
__author__ = 'xmduke'
from scrapy.cmdline import execute
import os,sys


sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(['scrapy','crawl','mobilepic'])




