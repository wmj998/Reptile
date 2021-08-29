import scrapy
from ..items import PptItem


class PptSpider(scrapy.Spider):
    name = 'ppt'
    allowed_domains = ['www.1ppt.com']
    start_urls = ['http://www.1ppt.com/']

    def parse(self, response):
        item_one = PptItem()
        li_ul = response.xpath('/html/body/div[5]/div/ul')
        for ul in li_ul:
            li_li = ul.xpath('./li')
            item_one['dirs_one'] = li_li[0].xpath('./text()').get()
            for li in li_li[1:]:
                dirs_two = li.xpath('./a/text()').get()
                if dirs_two:
                    item_tow = PptItem()
                    item_tow['dirs_one'] = item_one['dirs_one']
                    item_tow['dirs_two'] = dirs_two
                    url = 'http://www.1ppt.com' + li.xpath('./a/@href').get()
                    yield scrapy.Request(url=url, meta={'item': item_tow}, callback=self.parse_two)
                else:
                    li_a = li.xpath('./a')
                    for a in li_a:
                        item_tow = PptItem()
                        item_tow['dirs_one'] = item_one['dirs_one']
                        item_tow['dirs_two'] = a.xpath('./@title').get()
                        url = 'http://www.1ppt.com' + a.xpath('./@href').get()
                        yield scrapy.Request(url=url, meta={'item': item_tow}, callback=self.parse_two)

    def parse_two(self, response):
        li_li = response.xpath('/html/body/div/dl/dd/ul/li')
        for li in li_li:
            item = PptItem()
            item['dirs_one'] = response.meta['item']['dirs_one']
            item['dirs_two'] = response.meta['item']['dirs_two']
            name = li.xpath('./h2/a/text()').get()
            if name:
                item['name'] = name
            else:
                item['name'] = li.xpath('./h4/a/text()').get()
            url = 'http://www.1ppt.com' + li.xpath('./a/@href').get()
            yield scrapy.Request(url=url, meta={'item': item}, callback=self.parse_three)

    def parse_three(self, response):
        item = response.meta['item']
        url = 'http://www.1ppt.com' + response.xpath('/html/body/div[4]/div[1]/dl/dd/ul[1]/li/a/@href').get()
        yield scrapy.Request(url=url, meta={'item': item}, callback=self.parse_four)

    def parse_four(self, response):
        item = response.meta['item']
        item['url'] = response.xpath('/html/body/dl/dd/ul[2]/li[1]/a/@href').get()
        yield item

