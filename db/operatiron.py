# -*- conding: utf-8 -*-
__author__ = 'yueg'
import MySQLdb as db
import conn

class dbOperation():
    def __init__(self, con):
        self.conn = con

    def insert(self, sql):
        return self.conn.query(sql)

    def find(self, sql):
        return self.conn.query(sql)

    def update(self, sql):
        return self.conn.query(sql)

