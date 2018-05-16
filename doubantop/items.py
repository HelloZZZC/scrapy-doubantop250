#!/usr/bin/python
# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubantopItem(scrapy.Item):
    # define the fields for your item here like:
    picPath = scrapy.Field()
    rank = scrapy.Field()
    title = scrapy.Field()
    info = scrapy.Field()
    score = scrapy.Field()
    evaluateNum = scrapy.Field()
    inq = scrapy.Field()
