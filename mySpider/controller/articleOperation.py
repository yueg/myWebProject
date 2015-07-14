# -*- coding: utf-8 -*-
__author__ = 'yueg'

import db.conn as dbConn
import db.operatiron as dbOperation
import time

dbName = "VillageConstruction"
table = 'article'
doc_table = "document"
class articleOper():
    def __init__(self):
        self.conn = dbConn.mysqlConn(dbName).conn
        self.db = dbOperation.dbOperation(self.conn)

    def saveArticleToDB(self, title = "", pos1 = "", pos2 = "", pos3 = "", content = "", article_time = "", url = "", article_type = '0'):
        if self.isArticleExists(title):
            return False
        indexList = ['title', 'pos1', 'pos2', 'pos3', 'content', 'article_time', 'update_time', 'url', 'article_type']
        valueList = []
        valueList.append(title)
        valueList.append(pos1)
        valueList.append(pos2)
        valueList.append(pos3)
        valueList.append(content)
        valueList.append(article_time)
        valueList.append(time.strftime('%Y-%m-%d %X', time.localtime()))
        valueList.append(url)
        valueList.append(article_type)
        try:
            self.db.insertList(table, indexList, valueList)
            return True
        except:
            return False

    def saveDocToDB(self, article_id = '', doc_name = '', doc_dir = '', doc_desc = '', doc_url = '', doc_time = '', update_time = ''):
        indexList = ['article_id', 'doc_name', 'doc_dir', 'doc_desc', 'doc_url', 'doc_time', 'update_time']
        valueList = [article_id, doc_name, doc_dir, doc_desc, doc_url, doc_time, update_time]
        for i in range(len(valueList)):
            valueList[i] = valueList[i].encode('utf-8')
        try:
            return self.db.insertList(doc_table, indexList, valueList)
        except:
            return False

    def isArticleExists(self, title):
        articleInfo = self.getArticleInfoFromTitle(title)
        if not articleInfo:
            return False
        else:
            return True

    def getArticleInfoFromTitle(self, title):
        articleInfo = self.db.findEx(table, 'title', title)
        return articleInfo

    def getArticleIdFromTitle(self, title):
        articleId = self.getArticleInfoFromTitle(title)[0][0]
        return articleId