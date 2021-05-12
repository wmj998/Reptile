import requests
import re
from lxml import etree
from bs4 import BeautifulSoup
from pyquery import PyQuery as pq

response = requests.get('https://www.piaohua.com/html/kehuan/index.html')
response.encoding = response.apparent_encoding
html = response.text


# 正则
# for i in re.findall('<img src="(.*?)"', html):
#     print(i)


# XPath
# html = etree.parse(html, etree.HTMLParser())
# result = html.xpath('//img[@src]')
# print(result)


# BeautifulSoup
# soup = BeautifulSoup(html, 'lxml')
# for i in soup.select('img'):
#     print(i.attrs['src'])


# pyquery
# doc = pq(html)
# for i in doc('img').items():
#     print(i.attr('src'))
