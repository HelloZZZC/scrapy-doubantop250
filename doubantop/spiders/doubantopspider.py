# -*- coding: utf-8 -*-

import scrapy
import re
from bs4 import BeautifulSoup
from doubantop.items import DoubantopItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import sys

class DoubanTopSpider(CrawlSpider):
    name = 'doubantop'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250?start=0']
    rules = [
        Rule(LinkExtractor(allow=('movie.douban.com/top250\?start=\d*', )), callback='parse_content')
    ]

    def parse_content(self, response):
        reload(sys)
        sys.setdefaultencoding('utf-8')
        soup = BeautifulSoup(response.body, "lxml")
        li_list = soup.body.find(class_ = "article").find(class_ = "grid_view").find_all('li')
        for li in li_list:
            item = DoubantopItem()
            img = li.find(class_ = "item").find(class_ = "pic").a.img
            #图片地址
            item['picPath'] = img['src']
            #电影排名
            item['rank'] = li.find(class_ = "item").find(class_ = "pic").em.string
            #电影主标题
            spans = li.find(class_ = "item").find(class_ = "info").find(class_ = "hd").a.find_all('span')
            item['title'] = spans[0].string
            #电影信息
            info = li.find(class_ = "item").find(class_ = "info").find(class_ = "bd").p
            item['info'] = self.parseInfo(str(info)).strip()
            #电影评分
            starSpans = li.find(class_ = "item").find(class_ = "info").find(class_ = "bd").find(class_ = "star").find_all("span")
            item['score'] = starSpans[1].string
            #电影评价人数
            evaluateNum = starSpans[3].string
            item['evaluateNum'] = self.parseEvaluateNum(evaluateNum)
            #电影inq
            quote = li.find(class_ = "item").find(class_ = "info").find(class_ = "bd").find(class_ = "quote")
            if quote == None:
                item['inq'] = 'none inq'
            else:
                item['inq'] = quote.find(class_ = "inq").string
            yield item

    def parseInfo(self, content):
        return re.sub(r'<p(.*?)>|</p>|<br/>', '', content)

    def parseEvaluateNum(self, content):
        return re.sub(ur'[\u4e00-\u9fa5]', '', content)