# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NovelItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    book_name = scrapy.Field()
    book_title = scrapy.Field()
    chapter_num = scrapy.Field()
    chapter_name = scrapy.Field()
    chapter_url = scrapy.Field()
    text = scrapy.Field()
