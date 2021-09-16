import os
import re
import time
import requests
from multiprocessing import Pool


class PhSpider:
    def __init__(self):
        self.directory = 'temp/'
        self.url = 'https://www.piaohua.com/html/kehuan/list_{}.html'
        self.urls = [self.url.format(i) for i in range(1, 105)]
        self.headers = {
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)'
        }

    def get_html(self, url):
        res = requests.get(url=url, headers=self.headers)
        html = res.text
        self.get_url(html)

    def get_url(self, html):
        urls = re.findall('<img src="(.*?)"', html)[1:]
        for url in urls:
            self.get_picture(url)

    def get_picture(self, url):
        name = url.split('/')[-1]
        res = requests.get(url=url, headers=self.headers)
        img = res.content
        self.save_picture(name, img)

    def save_picture(self, name, img):
        if not os.path.exists(self.directory):
            os.mkdir(self.directory)
        with open(self.directory + name, 'wb') as f:
            f.write(img)

    def run(self):
        with Pool(processes=4) as pool:
            pool.map(self.get_html, self.urls)


if __name__ == '__main__':
    start_time = time.time()
    spider = PhSpider()
    spider.run()
    stop_time = time.time()
    times = stop_time - start_time
    print(times)
