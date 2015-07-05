__author__ = 'yueg'
import MySQLdb
import db.conn
import db.operatiron
import _mysql

dbConn = db.conn.mysqlConn("VillageConstruction")
conn = dbConn.conn
dbOperation = db.operatiron.dbOperation(conn)
print dbOperation.insert('insert into test values (2, "test")')