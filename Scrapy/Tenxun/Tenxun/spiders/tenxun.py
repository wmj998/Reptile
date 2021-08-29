import scrapy
import time
from ..items import TenxunItem


class TenxunSpider(scrapy.Spider):
    name = 'tenxun'
    allowed_domains = ['careers.tencent.com']
    keyword = input('搜索工作岗位：')
    start_urls = [f'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp={int(time.time() * 1000)}&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword={keyword}&pageIndex=1&pageSize=10&language=zh-cn&area=cn']

    def parse(self, response):
        html = response.json()
        count = html['Data']['Count']
        url = f'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp={int(time.time() * 1000)}&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword={self.keyword}&pageIndex=1&pageSize={count}&language=zh-cn&area=cn'
        yield scrapy.Request(url=url, callback=self.parse_two)

    def parse_two(self, response):
        html = response.json()
        for i in html['Data']['Posts']:
            url = 'https://careers.tencent.com/tencentcareer/api/post/ByPostId?timestamp=1630140318725&postId={}&language=zh-cn'.format(i['PostId'])
            yield scrapy.Request(url=url, callback=self.parse_three)

    def parse_three(self, response):
        html = response.json()
        item = TenxunItem()
        item['RecruitPostId'] = html['Data']['RecruitPostId']
        item['RecruitPostName'] = html['Data']['RecruitPostName']
        item['LocationName'] = html['Data']['LocationName']
        item['CategoryName'] = html['Data']['CategoryName']
        item['Responsibility'] = html['Data']['Responsibility']
        item['Requirement'] = html['Data']['Requirement']
        item['LastUpdateTime'] = html['Data']['LastUpdateTime']
        yield item

