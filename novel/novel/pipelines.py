# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.conf import settings
import pymongo

class NovelPipeline(object):
    def __init__(self):
        host = settings['MONGODB_HOST']
        port = settings['MONGODB_PORT']
        db = settings['MONGODB_DB']
        client = pymongo.MongoClient(host, port)
        tdb = client[db]
        self.post = tdb[settings['MONGODB_DOC']]

    def process_item(self, item, spider):
        book_info = dict(item)
        self.post.insert(book_info)

        return item
