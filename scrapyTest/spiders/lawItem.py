import scrapy

__author__ = 'dzwu'

class LawItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    updateTime = scrapy.Field()
    collection = scrapy.Field()
