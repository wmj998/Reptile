import threading
import time
import requests
import re


def phspider(url_p, num):
    for i in range(1, num):
        url = url_p.format(i)
        res = requests.get(url=url)
        html = res.text

        urls = re.findall('<img src="(.*?)"', html)
        for j in range(1, len(urls)):
            img = requests.get(url=urls[j])
            name = urls[j].split('/')[-1]
            f = open('tmp/'+name, 'wb')
            f.write(img.content)
            f.close()


url_p = 'https://www.piaohua.com/html/kehuan/list_{}.html'
num = 105

thread = threading.Thread(target=phspider, args=(url_p, num))
thread.start()

