# -*- coding: utf-8 -*-
from cssselect import Selector
import scrapy
from scrapyTest.spiders.ux265Item import Ux265Item


class Ux265spiderSpider(scrapy.Spider):
    name = "ux265Spider"
    allowed_domains = ["law.wkinfo.com.cn"]
    start_urls = ['http://law.wkinfo.com.cn/search/process?collection=legislation&navSelected=legislation&modules=&sp.pageSize=100&sp.order=important,promulgatingDate+desc&reserved_query=&viewType=list&sp.pageNo=1']

    for i in range(1,2):
        start_urls.append('http://law.wkinfo.com.cn/search/process?collection=legislation&navSelected=legislation&modules=&sp.pageSize=100&sp.order=important,promulgatingDate+desc&reserved_query=&viewType=list&sp.pageNo='+str(i))
    rules = {

    }

    def parse(self, response):
        # self.logger.info('A response from %s just arrived!', response.url)
        # self.logger.error('error',response.body)
        # for block in response.xpath('//div[id="bd"]/div/ul'):
        #     group = block.xpath('h2/text()').extract()
        #     for sub_block in block.xpath('li'):
        #         name = sub_block.xpath('a/text()').extract()
        #         link = sub_block.xpath('a/@href').extract()
        #         yield Ux265Item(name=name,link=link,group=group)

        hrefs = response.xpath('//h4/a/@href').extract()
        for href in hrefs:
            print(href)

