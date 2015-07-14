# -*- coding:utf8 -*-
__author__ = 'yueg'
import os
import _mysql as db

class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kwargs)
        return cls._instance


class mysqlConn(Singleton):
    def __init__(self, dbName):
        self.conn = db.connect(host="localhost", user="root", passwd="123456", db=dbName)
        self.conn.query("set names utf8")
