# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy_redis.spiders import RedisSpider
from scrapy.selector import Selector
from novel.items import NovelItem
from scrapy.http import Request


# class DaomubijiSpider(scrapy.Spider):
class DaomubijiSpider(RedisSpider):
    name = "daomubiji"
    # allowed_domains = ["http://www.daomubiji.com"]
    redis_key = 'nvospider:start_urls'
    start_urls = [
        'http://www.daomubiji.com/',
        #'http://www.daomubiji.com/qi-xing-lu-wang-01.html'
    ]

    def parse(self, response):
        selector = Selector(response)
        table = selector.xpath('//table')
        for each in table:
            book_name = each.xpath('tr/td[@colspan="3"]/center/h2/text()').extract()[0]
            print book_name
            contents = each.xpath('tr/td/a/text()').extract()
            urls = each.xpath('tr/td/a/@href').extract()
            for idx, content in enumerate(contents):
                content_list = content.split(' ')
                item = NovelItem()
                if len(content_list) == 2:
                    item['chapter_name'] = content_list[1][-3:]
                elif len(content_list) == 3 or len(content_list) > 4:
                    item['chapter_name'] = ' '.join(content_list[2:])
                elif len(content_list) == 4:
                    item['chapter_name'] = content_list[3]

                if len(content_list) < 4:
                    item['book_title'] = content_list[0]
                    item['chapter_num'] = content_list[1]
                else:
                    item['book_title'] = ' '.join(content_list[:2])
                    item['chapter_num'] = content_list[2]

                item['chapter_url'] = urls[idx]
                item['book_name'] = book_name
                print 'craw:', urls[idx]
                yield Request(urls[idx], callback="parseContent", meta={'item':item})
                # break
            # break


    def parseContent(self, response):
        # return
        selector = Selector(response)
        item = response.meta['item']
        html = selector.xpath('//div[@class="content"]').extract()[0]
        textField = re.search('<div style="clear:both"></div>(.*?)<div', html, re.S).group(1)
        text = re.findall('<p>(.*?)</pdff55>', textField, re.S)
        item['text'] = ''.join(text)
        print item['book_name']
        print item['book_title']
        print item['chapter_name']
        print item['chapter_num']
        print item['chapter_url']
        print 'crawed.'
        yield item
        # print html


