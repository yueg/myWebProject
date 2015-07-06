__author__ = 'yueg'
import operatiron
import conn
import MySQLdb as db
import mySpider.controller.articleOperation as articleOperation

artiOper = articleOperation.articleOper()
print artiOper.saveArticleToDB(title="test3", pos1="pos1", pos2="pos2", pos3 = "pos3", content="content", article_time="2011-11-11")
# print artiOper.isArticleExists('test3')

# sql = 'INSERT INTO article (title, pos1, pos2, pos3, content, article_time) VALUES ("test", "pos1", "pos2", "pos3", "content", "2011-11-11")'
db = conn.mysqlConn('mydb').conn
oper = operatiron.dbOperation(db)
#oper.insertList()
article_list = oper.find("select * from article")
print len(article_list)
for article in article_list:
    for temp in article:
        print temp