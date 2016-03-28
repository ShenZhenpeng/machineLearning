#coding:utf8
from scrapy.spiders import CrawlSpider
from scrapy.http import Request
from scrapy.selector import Selector
from douban.items import DoubanItem


class Douban(CrawlSpider):
    name = "douban"
    redis_key = 'douban:start_urls'
    start_urls = ['http://movie.douban.com/top250']

    url = "http://movie.douban.com/top250"

    def parse(self, response):
        item = DoubanItem()
        selector = Selector(response)
        Moives = selector.xpath('//div[@class="info"]')
        for eachMovie in Moives:
            titles = eachMovie.xpath('div[@class="hd"]/a/span/text()').extract()
            title = "".join(titles)

            movieinfo = eachMovie.xpath('div[@class="bd"]/p/text()').extract()
            full_info = ""
            for info in movieinfo:
                info = info.strip()
                if info != "":
                    full_info = full_info + "\n" + info

            star = eachMovie.xpath('div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()').extract()[0]
            quote = eachMovie.xpath('div[@class="bd"]/p/span/text()').extract()
            if quote:
                quote = quote[0]
            else:
                quote = ''

            item['title'] = title
            item['movieinfo'] = full_info
            item['star'] = star
            item['quote'] = quote

            yield item

            # 翻页
            next_link = eachMovie.xpath('//span[@class="next"]/link/@href').extract()
            if next_link:
                next_link = next_link[0]
                print next_link
                yield Request(self.url + next_link, callback=self.parse)