import requests
import re

response = requests.get('https://www.piaohua.com/html/kehuan/list_1.html')
text = response.text
urls = re.findall('<img src="(.*?)"', text)
for i in range(1, len(urls)):
    img = requests.get(urls[i])
    name = urls[i].split('/')[-1]
    f = open('tmp/'+name, 'wb')
    f.write(img.content)
    f.close()
