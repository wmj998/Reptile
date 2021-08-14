import random
import time
import requests
import pandas as pd
from lxml import etree


class MySpider:
    def __init__(self):
        self.url = 'https://maoyan.com/board/4?offset={}'
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Cookie': '__mta=246698939.1628517216167.1628864108380.1628925039675.35; uuid_n_v=v1; uuid=3059C420F91911EBB76BF980F269E62BCDA2D9FB13FB41C99CF0C347A028BCFF; _lxsdk_cuid=17b2b30ada4c8-0c2b1efb2ab7ca-4343363-144000-17b2b30ada4c8; _lxsdk=3059C420F91911EBB76BF980F269E62BCDA2D9FB13FB41C99CF0C347A028BCFF; _csrf=b48ed2960e8fa8bd0ff27077a3d2b96fb8106e16ff353c38ec9c20623a071e15; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1628781191,1628856353,1628860230,1628925029; _lx_utm=utm_source%3Dbing%26utm_medium%3Dorganic; __mta=246698939.1628517216167.1628864108380.1628925032038.35; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1628925040; _lxsdk_s=17b43ac5ef7-c7d-09d-91f%7C%7C1',
            'Host': 'maoyan.com',
            'Referer': 'https://maoyan.com/board',
            'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
            'sec-ch-ua-mobile': '?0',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
        }
        self.data = pd.DataFrame()

    def get_html(self, url):
        response = requests.get(url=url, headers=self.headers)
        html = response.text
        return html

    def parse_html(self, html):
        selector = etree.HTML(html)
        dd_list = selector.xpath('//*[@id="app"]/div/div/div[1]/dl/dd')

        item = {}
        for dd in dd_list:
            item['title'] = dd.xpath('./div/div/div[1]/p[1]/a/@title')[0]
            item['star'] = dd.xpath('./div/div/div[1]/p[2]/text()')[0].strip()
            item['releasetime'] = dd.xpath('./div/div/div[1]/p[3]/text()')[0]
            score = dd.xpath('./div/div/div[2]/p/i/text()')
            item['score'] = ''.join(score)
            item['href'] = 'https://maoyan.com' + dd.xpath('./div/div/div[1]/p[1]/a/@href')[0]
            print(item)
            self.data = self.data.append(item, ignore_index=True)

    def run(self):
        for i in range(0, 100, 10):
            url = self.url.format(i)
            html = self.get_html(url)
            self.parse_html(html)
            time.sleep(random.uniform(1, 2))
        self.data.to_excel('data.xlsx', index=False)


if __name__ == '__main__':
    spider = MySpider()
    spider.run()
