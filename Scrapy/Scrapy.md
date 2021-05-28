# Scrapy 项目



1. 创建项目 —— tutorial

   ```
   scrapy startproject tutorial
   ```

2. 创建 Spider —— quotes.py

   ```
   cd tutorial
   scrapy genspider quotes(Spider名称) quotes.toscrape.com(网站域名) 
   ```

3. 创建Item —— 修改 items.py 文件

4. 解析Response —— 修改 quotes.py 中的 parse() 方法

5. 运行

   + 创建 start.py 文件

     ```python
     from scrapy.cmdline import execute
     execute(['scrapy', 'crawl', 'quotes'])
     ```

   + 命令行

     ```
     scrapy crawl quotes
     ```

     

   



