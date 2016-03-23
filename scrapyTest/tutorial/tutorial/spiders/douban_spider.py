# -*- coding: utf-8 -*-

import scrapy
from tutorial.items import DoubanItem

class DoubanSpider(scrapy.spiders.Spider):
    name = "douban"
    allowed_domains = ["dmoz.org"]
    start_urls = ["https://movie.douban.com/"]

    def parse(self, response):
        print "#############################"
        print response.url
        for sel in response.xpath('//a'):
            item = DoubanItem()
            link =  sel.xpath('@href').extract()
            if len(link) > 0:
                link = link[0]
                if 'movie.douban.com/subject' in link:
                    link = link[:link.find('?')]
                    if link.find('cinema') > -1:
                        link =  link[:-6]
                    item['link'] = link
                    print item['link']
            yield item
