from django.db import models
from webDB import conn
from webDB import operatiron
# Create your models here.

# db = operatiron.dbOperation().conn

class articleModel():
    db = operatiron.dbOperation()
    table = 'article'

    def getArticleList(self, page = 1, num = 20, article_type = -1):
        ret = []
        if article_type == -1:
            sql = "SELECT * FROM " + self.table + " ORDER BY UNIX_TIMESTAMP(article_time) DESC LIMIT " + str((page - 1) * num) + ", " + str(num)
        else:
            sql = "SELECT * FROM " + self.table + " WHERE article_type = '" + str(article_type) + "' ORDER BY UNIX_TIMESTAMP(article_time) DESC LIMIT " + str((page - 1) * num) + ", " + str(num)
        try:
            ret = self.db.find(sql)
        except:
            pass
        return ret

    def getArticleInfoFromId(self, id):
        ret = []
        try:
            ret = self.db.findEx(self.table, 'id', id)
            return ret[0]
        except:
            return ret


    def getArticleNum(self, article_type = -1):
        ret = 0
        try:
            if article_type == -1:
                ret = self.db.getNum(self.table)
            else:
                ret = self.db.getNumByIndex(self.table, 'article_type', str(article_type))
        except:
            pass
        return ret

    def getMaxArticleId(self):
        sql = "SELECT MAX(id) FROM " + self.table
        try:
            return self.db.find(sql)[0][0]
        except:
            return 0

    def getMinArticleId(self):
        sql = "SELECT MIN(id) FROM " + self.table
        try:
            return self.db.find(sql)[0][0]
        except:
            return 0

