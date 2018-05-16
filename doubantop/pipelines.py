#!/usr/bin/python
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from doubantop.dbhelper import DbHelper
import time

class DoubantopPipeline(object):
    def process_item(self, item, spider):
        self.insert_item(item)
        return item

    def insert_item(self, item):
        sql = "INSERT INTO `movie` ( `title`, `picPath`, `rank`, `info`, `score`, `evaluateNum`, `inq`, `createdTime`, `updatedTime`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        params = (item['title'], item['picPath'], item['rank'], item['info'], item['score'], item['evaluateNum'], item['inq'], int(time.time()), int(time.time()))
        dbHelper = DbHelper()
        dbHelper.excuteSql(sql, params)
