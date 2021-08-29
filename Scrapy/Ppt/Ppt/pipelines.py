# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import os

import scrapy
from itemadapter import ItemAdapter
from scrapy.pipelines.files import FilesPipeline


class PptPipeline(FilesPipeline):
    def get_media_requests(self, item, info):
        yield scrapy.Request(url=item['url'], meta={'item': item})

    def file_path(self, request, response=None, info=None, *, item=None):
        item = request.meta['item']
        filename = '{}/{}/{}{}'.format(
            item['dirs_one'],
            item['dirs_two'],
            item['name'],
            os.path.splitext(item['url'])[1]
        )
        return filename
