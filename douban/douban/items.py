# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

# import scrapy
from scrapy import Item, Field

class DoubanItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    title = Field()
    movieinfo = Field()
    star = Field()
    quote = Field()
