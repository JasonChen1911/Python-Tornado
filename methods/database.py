# -*- coding:utf8 -*-

import MySQLdb

#连接数据库
db=MySQLdb.connect("localhost", "root", "root147258", "Tornado", charset='utf8')
cursor = db.cursor()

