import json
import requests

url = 'https://fake-useragent.herokuapp.com/browsers/0.1.11'
headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)'
}
res = requests.get(url=url, headers=headers)
html = res.json()
with open('ua.json', 'w') as f:
    json.dump(html, f)

