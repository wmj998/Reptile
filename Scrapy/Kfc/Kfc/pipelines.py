# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymongo
from .settings import *
from itemadapter import ItemAdapter


class KfcPipeline:
    def process_item(self, item, spider):
        print(item)
        return item


class KfcMongoPipeline:
    def open_spider(self, spider):
        self.con = pymongo.MongoClient(host=MONGO_HOST, port=MONGO_PORT)
        self.db = self.con[MONGO_DB]
        self.set = self.db[MONGO_SET]

    def process_item(self, item, spider):
        d = dict(item)
        self.set.insert_one(d)
        return item
