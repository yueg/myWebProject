# -*- coding: utf-8 -*-
__author__ = 'yueg'

import re

import scrapy
from bs4 import BeautifulSoup as bsp

from mySpider.items import TownspiderItem
import db.conn as dbConn
import controller.articleOperation as articleOperation

class TownSpider(scrapy.Spider):
    artiOper = articleOperation.articleOper()
    name = "town"
    allowed_domains = ["mohurd.gov.cn"]
    start_urls = [
        "http://www.mohurd.gov.cn/cxgh/zcfb/index.html",
        "http://www.mohurd.gov.cn/cxgh/hydt/index.html",
        "http://www.mohurd.gov.cn/cxgh/cxghdfxx/index.html",
        # "http://www.mohurd.gov.cn/wjfb/200611/t20061101_156871.html"
    ]

    def parse(self, response):
        sel = scrapy.Selector(response)
        #获取页面信息
        content = response.body

        #获取当前页面url
        url = response.url.encode('utf-8')

        #创建soup对象
        soup = bsp(content)

        #获取标题信息
        title = sel.xpath(("//html/head/title/text()")).extract()[0]
        # print title

        #获取当前位置
        pos_all = soup.find_all(href = re.compile("/index.html"))
        for temp in pos_all:
            #print temp.string
            if temp.string == u'首页':
                current_position = temp
                break
        pos_str = ''
        for temp in current_position.parent:
            pos_str += temp.string
        pos_str.strip()
        pos_list = pos_str.split('>')
        pos_list = pos_list[1:]

        item = TownspiderItem()
        item['url'] = url
        item['title'] = title

        # yield item

        #获取文档时间
        url_split = url.strip().split('/')
        url_last = url_split[-1]
        url_time = url_last.split('.')[0]
        if url_time[0] == 't':
            url_time = url_time.split('_')[0][1:]

            #获取文档正文
            content = soup.find_all('div', class_ = 'union')
            article_content = ''
            for cont in content:
                for temp in cont.contents:
                    if temp.string == None:
                        if temp.name == 'p':
                            for small_temp in temp.contents:
                                if small_temp.string == None:
                                    continue
                                elif small_temp.name == 'style':
                                    continue
                                else:
                                    article_content += small_temp.string
                            continue
                        else:
                            continue
                    article_content += temp.string
            # print article_content

            for i in range(len(pos_list)):
                pos_list[i] = pos_list[i].encode('utf-8')
            if len(pos_list) == 1:
                pos1 = pos_list[0]
                pos2 = ''
                pos3 = ''
            elif len(pos_list) == 2:
                pos1, pos2 = pos_list
                pos3 = ''
            elif len(pos_list) >= 3:
                pos1, pos2, pos3 = pos_list
            if pos1 == '政策发布':
                article_type = 1
            elif pos1 == '公示公告':
                article_type = 2
            elif pos1 == '领导动态':
                article_type = 3
            elif pos1 == '行业动态':
                article_type = 4
            elif pos1 == '地方动态':
                article_type = 5
            else:
                article_type = 0
            if title:
                title = title.encode('utf-8')
            if article_content:
                article_content = article_content.encode('utf-8')
            if url_time:
                url_time = url_time.encode('utf-8')
                url_time = url_time[0:4] + '-' + url_time[4:6] + '-' + url_time[6:8] + ' 00:00:00'
            # print article_content
            try:
                self.artiOper.saveArticleToDB(title=title, pos1 = pos1, pos2=pos2, pos3=pos3, content=article_content, article_time=url_time, url = url, article_type = str(article_type))
            except:
                print title, pos1, pos2, pos3, article_content, url_time, url

        if len(pos_list) == 2:
            for link in sel.xpath('//span/a/@href').extract():
                request = scrapy.Request(link, callback=self.parse)
                yield request

            for article_link in sel.xpath(("//tr/td/a/@href")).extract():
                if article_link[0] == '/':
                    continue
                article_request = scrapy.Request(article_link, callback=self.parse)
                yield article_request

        #for link in sel.xpath()

        def dbOperation(sql):
            conn = dbConn('yueg')
            db = dbOperation(conn)
            try:
                db.insert(sql)
            except:
                print "DB operation error: ", sql
