# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PptItem(scrapy.Item):
    # define the fields for your item here like:
    dirs_one = scrapy.Field()
    dirs_two = scrapy.Field()
    name = scrapy.Field()
    url = scrapy.Field()


