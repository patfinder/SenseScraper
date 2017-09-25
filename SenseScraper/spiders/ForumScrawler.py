# -*- coding: utf-8 -*-
from uu import encode

import scrapy

class ForumcrawlerSpider(scrapy.Spider):
    name = 'ForumCrawler'
    allowed_domains = ['tinhte.vn']
    start_urls = ['https://tinhte.vn/threads/2730624/']

    def parse(self, response):
        selectors = response.xpath('//*[contains(concat(" ", @class, " "), " baseHtml ")]')
        posts = [" ".join(s.select('./text()').extract()) for s in selectors[1:]]
        for p in posts:
            yield {"PostZ": p.encode("utf8")}

    @staticmethod
    def selectClass(response, class1):
        response.xpath()
        pass
