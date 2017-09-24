# -*- coding: utf-8 -*-
import scrapy

class ForumcrawlerSpider(scrapy.Spider):
    name = 'ForumCrawler'
    allowed_domains = ['tinhte.vn']
    start_urls = ['https://tinhte.vn/threads/2730624/']

    def parse(self, response):
        return response.xpath("//ol[contains(@class, 'messageList')]/li/text()")

    @staticmethod
    def selectClass(response, class1):
        response.xpath()
        pass
