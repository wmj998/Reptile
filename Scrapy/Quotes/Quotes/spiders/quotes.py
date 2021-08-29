import scrapy

from ..items import QuotesItem


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = [f'https://quotes.toscrape.com/page/{i}/' for i in range(1, 11)]

    def parse(self, response):
        div_list = response.xpath('/html/body/div/div[2]/div[1]/div')
        for div in div_list:
            item = QuotesItem()
            item['text'] = div.xpath('./span[1]/text()').get()
            item['author'] = div.xpath('./span[2]/small/text()').get()
            item['tags'] = ','.join(div.xpath('./div/a/text()').extract())
            yield item


# class QuotesSpider(scrapy.Spider):
#     name = 'quotes'
#     allowed_domains = ['quotes.toscrape.com']
#     start_urls = ['https://quotes.toscrape.com/page/1/']
#     page = 1
#
#     def parse(self, response):
#         div_list = response.xpath('/html/body/div/div[2]/div[1]/div')
#         for div in div_list:
#             item = QuotesItem()
#             item['text'] = div.xpath('./span[1]/text()').get()
#             item['author'] = div.xpath('./span[2]/small/text()').get()
#             item['tags'] = div.xpath('./div/a/text()').get()
#             yield item
#
#         if self.page < 10:
#             self.page += 1
#             url = f'https://quotes.toscrape.com/page/{self.page}/'
#             yield scrapy.Request(url=url, callback=self.parse)


'''
多线程：重写start_requests()和另写parse()方法
'''
