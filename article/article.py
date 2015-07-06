# -*- coding: utf-8 -*-
__author__ = 'yueg'

class article_info():
    def __init__(self, article):
        self.id = article[0]
        self.article_type = article[1]
        self.class_id = article[2]
        self.url = article[3]
        self.pos1 = article[4]
        self.pos2 = article[5]
        self.pos3 = article[6]
        self.title = article[7]
        self.content = article[8]
        self.article_time = article[9]
        self.update_time = article[10]
        self.is_display = article[11]
        self.is_doc = article[12]
        self.is_img = article[13]

        self.pos = self.pos1
        # if self.pos2:
        #     self.pos += '-' + self.pos2
        # if self.pos3:
        #     self.pos += '-' + self.pos3

        title_temp = self.title.split('-')
        self.title = title_temp[-1].strip()

        self.article_time = self.article_time[0:4] + '-' + self.article_time[4:6] + '-' + self.article_time[6:8]

class article_head():
    def __init__(self, article):
        article_c = article_info(article)
        self.title = article_c.title
        self.url = article_c.url
        self.article_time = article_c.article_time
        self.pos = article_c.pos


