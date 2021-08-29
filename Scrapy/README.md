# Scrapy 项目



1. 创建项目 —— Quotes

   ```
   scrapy startproject Quotes
   ```

2. 创建 Spider —— quotes.py

   ```
   cd Quotes
   scrapy genspider quotes(Spider名称) quotes.toscrape.com(网站域名)
   ```

3. 定义数据结构 —— items.py

4. 解析 response 提取数据 —— quotes.py

5. 管道 —— pipelines.py

6. 中间件 —— middlewares.py

7. 全局配置 —— settings.py

8. 运行

   + 创建 run.py —— Quotes 目录下

     ```python
     from scrapy.cmdline import execute
     execute(['scrapy', 'crawl', 'quotes'])
     # execute('scrapy crawl quotes'.split())
     ```

   + 命令行

     ```
     scrapy crawl quotes
     ```




   ## Daomu

   多级页面



   ## Kfc

   POST



   ## Picture

   图片



   ## Ppt

   文件



## Tenxun

分布式

   

   



