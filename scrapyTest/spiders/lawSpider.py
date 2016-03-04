# -*- coding: utf-8 -*-
import re
import urlparse

from cssselect import Selector
import datetime
import scrapy
from scrapy.spiders import CrawlSpider
from scrapy.http.request import Request
import time
from scrapyTest.spiders.lawItem import LawItem


class LawSpider(scrapy.Spider):
    name = "lawSpider"
    allowed_domains = ["law.wkinfo.com.cn"]
    # def start_requests(self):
    #     requestList = []
    #     for i in range(1,2):
    #         requestList.append(scrapy.Request('http://law.wkinfo.com.cn/search/process?collection=legislation&navSelected=legislation&modules=&sp.pageSize=100&sp.order=important,promulgatingDate+desc&reserved_query=&viewType=list&sp.pageNo='+str(i), self.parse))
    #     return requestList
    start_urls = []
    collections = {'legislation':3000,'case':5000,'caseAnalysis':500,'treaty':500,'article':500,'adminPenalty':500,'utilityWriting':500,'expertAnswer':500,'news':500}
    baseUrl = 'http://law.wkinfo.com.cn/search/process?collection=#collection#&sp.pageSize=100&&viewType=list&sp.pageNo='
    for key, value in collections.items():
        url = baseUrl.replace('#collection#',key)
        pageNo = value/100+1
        for i in range(1,pageNo):
            start_urls.append(url+str(i))

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, cookies={'JSESSIONID':'B9943EFD2E58ECF76AC56942E4F86624','bold_law_pass':'0x010000002daae753c263a21ea3734837f2ffc3eedd873326c4d7293befbf47f484d510f1','bold_law_user':'c3RhZmZjaGluYQ=='})

    def parse(self, response):
        items=[]
        username = response.xpath('//span[@class="user-tools-name"]/text()').extract()
        print(username)
        links = response.xpath('//h4/a')
        for link in links:
            item=LawItem()
            href = ''.join(link.xpath('@href').extract())

            item['link'] = href
            title = ''.join(link.xpath('text()').extract()).replace("\r\n","").strip()
            item['title'] = title
            match = re.search(r"collection=([\w]+)&", href)
            if match:
                result = match.group(1)
            else:
                result = ""
            item['collection'] = result
            if result:
                items.append(item)
        print(items.__len__())
        return items

