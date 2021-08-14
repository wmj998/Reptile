import hashlib
import random
import time
import requests


class YdSpider:
    def __init__(self):
        self.input_info = input('请输入需要翻译的内容：')
        self.url = 'https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
        self.headers = {
            'Cookie': 'DICT_UGC=be3af0da19b5c5e6aa4e17bd8d90b28a|; OUTFOX_SEARCH_USER_ID=-1917975282@222.211.238.82; JSESSIONID=abcyO3nFcAGjs908MDdTx; OUTFOX_SEARCH_USER_ID_NCOO=1973444275.2303727; ___rl__test__cookies=1628936215509',
            'Referer': 'https://fanyi.youdao.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
        }

    def md5_sign(self, sign):
        m = hashlib.md5()
        m.update(sign.encode())
        return m.hexdigest()

    def get_data(self):
        lts = str(int(time.time()*1000))
        salt = lts + str(random.randint(0, 9))
        sign = self.md5_sign("fanyideskweb" + self.input_info + salt + "Y2FYu%TNSbMCxc3t2u^XT")
        data = {
            'i': self.input_info,
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': salt,
            'sign': sign,
            'lts': lts,
            'bv': 'eda468fc64295ecf2810ab8a672c2db1',
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_REALTlME',
        }
        return data

    def get_html(self):
        data = self.get_data()
        res = requests.post(url=self.url, headers=self.headers, data=data)
        html = res.json()
        return html

    def run(self):
        html = self.get_html()
        print(html['translateResult'][0][0]['tgt'])


if __name__ == '__main__':
    spider = YdSpider()
    spider.run()
