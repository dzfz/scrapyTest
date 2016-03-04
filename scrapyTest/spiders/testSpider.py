# -*- coding: utf-8 -*-
import scrapy


class TestspiderSpider(scrapy.Spider):
    name = "testSpider"
    allowed_domains = ["law.wkinfo.com.cn"]
    start_urls = (
        'http://www.law.wkinfo.com.cn/',
    )

    def parse(self, response):
        pass
