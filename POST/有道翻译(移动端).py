import requests
from lxml import etree

input_text = input('请输入：')
url = 'http://m.youdao.com/translate'
data = {
    'inputtext': input_text,
    'type': 'AUTO'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
}
response = requests.post(url=url, data=data, headers=headers)
html = response.text
selector = etree.HTML(html)
result = selector.xpath('//*[@id="translateResult"]/li/text()')[0].strip()
print(result)
