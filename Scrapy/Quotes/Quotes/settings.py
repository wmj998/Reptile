# Scrapy settings for Quotes project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'Quotes'

SPIDER_MODULES = ['Quotes.spiders']
NEWSPIDER_MODULE = 'Quotes.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'Quotes (+http://www.yourdomain.com)'

# Obey robots.txt rules
# 君子协议
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# 配置 Scrapy 执行的最大并发请求数
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# 为同一网站的请求配置延迟
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# 取消注释，即开启Cookie
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    # 'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)',
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#     'Quotes.middlewares.QuotesSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'Quotes.middlewares.QuotesDownloaderMiddleware': 543,
    'Quotes.middlewares.QuotesDownloaderUaMiddleware': 200,
    # 'Quotes.middlewares.QuotesDownloaderProxyMiddleware': 200,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# 开启管道
ITEM_PIPELINES = {
    # '项目包名.模块名.类名': 优先级(1-1000，数字越小，优先级越高)
    'Quotes.pipelines.QuotesPipeline': 300,
    # 'Quotes.pipelines.QuotesMysqlPipeline': 100,
    # 'Quotes.pipelines.QuotesMongoPipeline': 200,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

MYSQL_HOST = 'localhost'
MYSQL_PORT = 3306
MYSQL_USER = 'root'
MYSQL_PWD = 'w_f1216570180'
MYSQL_DB = 'scrapy'
CHARSET = 'utf8'

MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_DB = 'scrapy'
MONGO_SET = 'quotes'

# 设置数据导出的编码
# csv 中文
# FEED_EXPORT_ENCODING = 'gb18030'
# csv 文件
# FEED_EXPORT_ENCODING = 'gbk'
# json 文件
# FEED_EXPORT_ENCODING = 'utf-8'

# 设定日志级别：DEBUG < INFO < WARNING < ERROR < CRITICAL
# LOG_LEVEL = 'INFO'
# LOG_FILE = 'quotes.log'
