from django.db import models
from webDB import conn
from webDB import operatiron
# Create your models here.

# db = operatiron.dbOperation().conn

class articleModel():
    db = operatiron.dbOperation()
    table = 'article'

    def getArticleList(self, page = 1, num = 20):
        ret = []
        sql = "SELECT * FROM " + self.table + " LIMIT " + str((page - 1) * num) + ", " + str(num)
        try:
            ret = self.db.find(sql)
        except:
            pass
        return ret

    def getArticleInfoFromId(self, id):
        ret = []
        try:
            ret = self.db.findEx(self.table, 'id', id)
        except:
            pass
        return ret

    def getArticleNum(self):
        ret = 0
        try:
            ret = self.db.getNum(self.table)
        except:
            pass
        return ret

