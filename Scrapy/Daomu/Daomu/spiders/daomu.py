import scrapy
from ..items import DaomuItem


class DaomuSpider(scrapy.Spider):
    name = 'daomu'
    allowed_domains = ['www.daomubiji.com']
    start_urls = ['http://www.daomubiji.com/']

    # def parse(self, response):
    #     li_article = response.xpath('//li[contains(@id,"menu-item-")]/a')
    #     for a in li_article:
    #         item = DaomuItem()
    #         item['homebook'] = a.xpath('./text()').get()
    #         url = a.xpath('./@href').get()
    #         yield scrapy.Request(url=url, meta={'item': item}, callback=self.parse_two)

    def parse(self, response):
        li_homebook = response.xpath('//article/div/h2/text()').extract()
        li_url = response.xpath('//article/p/a/@href').extract()
        for i in zip(li_homebook, li_url):
            item = DaomuItem()
            item['homebook'] = i[0]
            url = i[1]
            yield scrapy.Request(url=url, meta={'item': item}, callback=self.parse_two)

    def parse_two(self, response):
        li_article = response.xpath('/html/body/section/div[2]/div/article')
        for a in li_article:
            item = DaomuItem()
            item['homebook'] = response.meta['item']['homebook']
            item['excerpts'] = a.xpath('./a/text()').get()
            url = a.xpath('./a/@href').get()
            yield scrapy.Request(url=url, meta={'item': item}, callback=self.parse_three)

    def parse_three(self, response):
        item = response.meta['item']
        content = response.xpath('/html/body/section/div[1]/div/article/p/text()').extract()
        item['content'] = '\n'.join(content)
        yield item
