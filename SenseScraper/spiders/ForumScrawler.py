# -*- coding: utf-8 -*-
from uu import encode

import urlparse
import scrapy

class ForumcrawlerSpider(scrapy.Spider):
    name = 'ForumCrawler'
    allowed_domains = ['tinhte.vn']
    base_url = 'https://tinhte.vn/'
    # start_urls = ['https://tinhte.vn/threads/2730624/']
    # start_urls = ['https://tinhte.vn/threads/2730624/page-2']
    start_urls = ['https://tinhte.vn/threads/2731972/']

    runCount = 0

    def __init__(self, category='', domain=None, *args, **kwargs):
        super(ForumcrawlerSpider, self).__init__(*args, **kwargs)
        self.start_urls = ['http://www.example.com/categories/%s' % category]
        self.domain = domain

    def parse(self, response):

        ForumcrawlerSpider.runCount += 1

        selectors = response.xpath('//*[contains(concat(" ", @class, " "), " baseHtml ")]')
        # Skip first item which is the post
        posts = [" ".join(s.xpath('./text()').extract()) for s in selectors[1:]]
        for p in posts:
            yield {"PostZ": p.encode("utf8").strip()}

        # if ForumcrawlerSpider.runCount >= 5:
        #     return

        # Find next page URL
        linkSels = response.xpath('//*[contains(concat( " ", @class, " " ), " PageNav ")]//a[text() = "Sau >"]/@href')
        yield scrapy.Request(urlparse.urljoin(ForumcrawlerSpider.base_url, linkSels.extract_first())) if linkSels else None

    @staticmethod
    def selectClass(response, class1):
        response.xpath()
        pass
