import re
import time
import requests
from queue import Queue
from threading import Thread, current_thread, Lock


class PhSpider:
    def __init__(self):
        self.q = Queue()
        self.lock = Lock()

    def url_in(self):
        for i in range(1, 105):
            url = f'https://www.piaohua.com/html/kehuan/list_{i}.html'
            self.q.put(url)

    def get_html(self):
        while True:
            self.lock.acquire()
            if not self.q.empty():
                url = self.q.get()
                self.lock.release()
                res = requests.get(url=url)
                html = res.text
                self.get_url(html)
            else:
                self.lock.release()
                break

    def get_url(self, html):
        urls = re.findall('<img src="(.*?)"', html)[1:]
        for url in urls:
            self.get_picture(url)

    def get_picture(self, url):
        name = url.split('/')[-1]
        res = requests.get(url=url)
        img = res.content
        self.save_picture(name, img)

    def save_picture(self, name, img):
        with open('tmp/' + name, 'wb') as f:
            f.write(img)

    def run(self):
        self.url_in()
        for i in range(20):
            thread = Thread(target=self.get_html)
            thread.start()


if __name__ == '__main__':
    spider = PhSpider()
    spider.run()
