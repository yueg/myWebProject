# -*- coding: utf-8 -*-
__author__ = 'yueg'
from models import articleModel
from article import article_head

class document():
    article_instance = articleModel()
    def __init__(self, document_info):
        self.id = document_info[0]
        self.article_id = document_info[1]
        self.doc_name = document_info[2]
        self.doc_dir = document_info[3]
        self.doc_desc = document_info[4]
        self.doc_url = document_info[5]
        self.doc_time = document_info[6]
        self.update_time = document_info[7]
        self.link = self.doc_dir + self.doc_name
        self.doc_time = self.doc_time[0:10]
        self.update_time = self.update_time[0:10]

        article_info = self.article_instance.getArticleInfoFromId(self.article_id)
        self.article = article_head(article_info)

