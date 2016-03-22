# -*- coding: utf-8 -*-

import scrapy

class DoubanSpider(scrapy.spiders.Spider):
    name = "douban"
    allowed_domains = ["dmoz.org"]
    start_urls = ["https://movie.douban.com/"]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        print response.url
        # print response.body
        # with open(filename, 'wb') as f:
        #     f.write(response.body)