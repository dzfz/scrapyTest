# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb
import datetime
from scrapy.exceptions import DropItem


class ScrapytestPipeline(object):
    def __init__(self):
        try:
            self.db = MySQLdb.connect(host="127.0.0.1", user="root", passwd="root", port=3306, db="sitemap",  charset="utf8")
            self.cursor = self.db.cursor()
            print "Connect to db successfully!"

        except:
            print "Fail to connect to db!"

    def process_item(self, item, spider):
        if item:
            link = 'http://law.wkinfo.com.cn'+item['link']
            param = (item['title'], link, item['collection'],datetime.datetime.now())
            sql = "insert into documents (title,link,collection,updateTime) values(%s,%s,%s,%s)"
            self.cursor.execute(sql, param)
        else:
            raise DropItem(item)
        return item


    def close_spider(self, spider):
        self.db.commit()
        self.db.close
        print("Done")
