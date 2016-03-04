# -*- coding: utf-8 -*-
import scrapy


class WkSpider(scrapy.Spider):
    name = "wk"
    allowed_domains = ["law.wkinfo.com.cn"]
    start_urls = (
        'http://www.law.wkinfo.com.cn/',
    )

    def parse(self, response):
        pass
