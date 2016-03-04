import scrapy

__author__ = 'dzwu'

class Ux265Item(scrapy.Item):
    name = scrapy.Field()
    link = scrapy.Field()
    group = scrapy.Field()
