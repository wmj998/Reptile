import json

import scrapy

from ..items import PictureItem


class PictureSpider(scrapy.Spider):
    name = 'picture'
    allowed_domains = ['image.so.com']
    start_urls = [f'https://image.so.com/zjl?ch=beauty&sn={i}/' for i in range(0, 181, 30)]

    def parse(self, response):
        html = json.loads(response.text)
        for image in html['list']:
            item = PictureItem()
            item['name'] = image['title']
            item['url'] = image['qhimg_url']
            yield item

