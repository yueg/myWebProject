# _*_ coding: utf-8 -*-
__author__ = 'yueg'

import scrapy
from scrapy.loader import ItemLoader, Identity
from mySpider.items import TownspiderItem
from bs4 import BeautifulSoup as bsp

class TownSpider(scrapy.Spider):
    name = "town"
    allowed_domains = ["mohurd.gov.cn/cxgh"]
    start_urls = [
        "http://www.mohurd.gov.cn/cxgh/index.html",
    ]

    def parse(self, response):
        sel = scrapy.Selector(response)
        print "-----------------------1----------------------------"
        #获取页面信息
        content = response.body

        #创建soup对象
        soup = bsp(content)

        #获取标题信息
        title = soup.html.head.title.string

        #获取当前位置
        print title
        #print soup.prettify()
        print "-----------------------2----------------------------"
        #for link in sel.xpath()