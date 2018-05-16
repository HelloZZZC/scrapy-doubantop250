#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb
from scrapy.utils.project import get_project_settings
import time

class DbHelper():
    def __init__(self):
        self.settings = get_project_settings()
        self.host = self.settings['MYSQL_HOST']
        self.port = self.settings['MYSQL_PORT']
        self.user = self.settings['MYSQL_USER']
        self.passwd = self.settings['MYSQL_PASSWORD']
        self.db = self.settings['MYSQL_DBNAME']

    def connection(self):
        conn = MySQLdb.connect(
            host = self.host,
            user = self.user,
            passwd = self.passwd,
            db = self.db
        )
        return conn

    def excuteSql(self, sql, params):
        conn = self.connection();
        cur = conn.cursor()
        cur.execute(sql,params)
        conn.commit()
        cur.close()
        conn.close()

if __name__ == '__main__':
    sql = "INSERT INTO `movie` ( `title`, `picPath`, `rank`, `info`, `score`, `evaluateNum`, `inq`, `createdTime`, `updatedTime`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    params = ('测试电影', '//www.baidu.com/img/bd_logo1.png', '1', '测试', '9.9', '12345', '测试', int(time.time()), int(time.time()))
    dbHelper = DbHelper()
    dbHelper.excuteSql(sql, params)