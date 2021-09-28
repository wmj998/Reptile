import requests
import re
from lxml import etree
from bs4 import BeautifulSoup
from pyquery import PyQuery as pq

response = requests.get('https://www.piaohua.com/html/kehuan/index.html')
response.encoding = response.apparent_encoding
html = response.text


# 正则表达式
# for i in re.findall('<img src="(.*?)"', html):
#     print(i)


# XPath
# selector = etree.HTML(html)
# for i in selector.xpath('//img/@src'):
#     print(i)


# BeautifulSoup
# soup = BeautifulSoup(html, 'lxml')
# for i in soup.select('img'):
#     print(i.attrs['src'])


# pyquery
# doc = pq(html)
# for i in doc('img').items():
#     print(i.attr('src'))
