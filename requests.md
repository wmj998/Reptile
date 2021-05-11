## requests

```python
import requests
```



- 文件上传

  ```python
  files = {'file': open(path, 'rb')}
  r = requests.post(url, files=files)
  print(r.text)
  ```

- SSL 证书验证

  ```python
  r = requests.get(url, verify=False)
  ```

- 代理设置

  ```python
  proxies = {'http':'http: I 110 .10.1.10: 3128',
             'https'·'http: //10.10.1.10: 1080'}
  r = requests.get(url, proxies=proxies)
  ```

- 身份认证

  ```python
  r = requests.get(url, auth=('username ', 'password'))
  ```

- Prepared Request 构造POST请求

  ```python
  from requests import Request, Session
  
  data = {
      'name ': 'names'
  }
  headers = {
      'User-Agent ': ' '
  }
  s = Session()
  req = Request('POST', url, data=data, headers=headers)
  prepped = s.prepare_request(req)
  r = s.send(prepped)
  print(r.text)
  ```

  

