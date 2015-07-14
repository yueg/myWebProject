# -*- coding:utf8 -*-
__author__ = 'yueg'


class dbOperation():
    def __init__(self, con):
        self.conn = con

    def query(self, sql):
        try:
            self.conn.query(sql)
            return True
        except:
            return False

    def insert(self, sql):
        return self.conn.query(sql)

    def update(self, sql):
        try:
            self.conn.query(sql)
            return True
        except:
            return False

    def delete(self, sql):
        try:
            self.conn.query(sql)
            return True
        except:
            return False

    def find(self, sql):
        self.conn.query(sql)
        r = self.conn.store_result()
        ret = []
        result_list = r.fetch_row()
        while result_list:
            if result_list:
                ret.append(result_list[0])
                result_list = r.fetch_row()
            else:
                break
        return ret

    def findEx(self, table, index, value):
        sql = "SELECT * FROM " + table + " WHERE " + index + "= '" + value + "'"
        return self.find(sql)

    def insertList(self, table, indexList, valueList):
        if len(indexList) != len(valueList):
            print "data format do not matching"
            return False
        for i in range(len(valueList)):
            valueList[i] = '"' + valueList[i] + '"'
        index = ', '.join(indexList)
        value = ', '.join(valueList)
        sql = "INSERT INTO " + table + " (" + index + ") VALUES (" + value + ")"
        try:
            self.conn.query(sql)
            return True
        except:
            print "Inserting data error"
            return False

    def updateList(self, table, indexList, valueList):
        if len(indexList) != len(valueList):
            print "data format do not matching"
            return False
        sql = "UPDATE " + table + "SET "
        for i in range(len(indexList)):
            sql += indexList[i] + " = '" + valueList[i] + "', "
        sql = sql[:-3]
        try:
            self.conn.query(sql)
            return True
        except:
            print "Updating data error"
            return False

    def delete(self, table, index, value):
        sql = "DELETE FROM " + table + " WHERE " + index + " = " + value
        try:
            self.conn.query(sql)
            return True
        except:
            return False

