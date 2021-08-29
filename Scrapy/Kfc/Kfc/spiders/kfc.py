import math
import scrapy
from ..items import KfcItem


class KfcSpider(scrapy.Spider):
    name = 'kfc'
    allowed_domains = ['www.kfc.com.cn']
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    keyword = input('餐厅关键字：')

    def start_requests(self):
        formdata = {
            'cname': '',
            'pid': '',
            'keyword': self.keyword,
            'pageIndex': '1',
            'pageSize': '10',
        }
        yield scrapy.FormRequest(url=self.url, formdata=formdata, callback=self.get_pages)

    def get_pages(self, response):
        html = response.json()
        pages = math.ceil(html['Table'][0]['rowcount']/10)
        for page in range(1, pages+1):
            formdata = {
                'cname': '',
                'pid': '',
                'keyword': self.keyword,
                'pageIndex': str(page),
                'pageSize': '10',
            }
            yield scrapy.FormRequest(url=self.url, formdata=formdata, callback=self.parse, dont_filter=True)

    def parse(self, response):
        html = response.json()
        for i in html['Table1']:
            item = KfcItem()
            item['rownum'] = i['rownum']
            item['addressDetail'] = i['addressDetail']
            item['cityName'] = i['cityName']
            item['provinceName'] = i['provinceName']
            item['storeName'] = i['storeName']
            yield item

