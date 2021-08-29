# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymongo
import pymysql

from .settings import *
from itemadapter import ItemAdapter


class QuotesPipeline:
    def process_item(self, item, spider):
        print(item)
        return item


class QuotesMysqlPipeline:
    def open_spider(self, spider):
        self.db = pymysql.connect(host=MYSQL_HOST, port=MYSQL_PORT, user=MYSQL_USER,
                                  password=MYSQL_PWD, database=MYSQL_DB, charset=CHARSET)
        self.cur = self.db.cursor()

    def process_item(self, item, spider):
        ins = 'insert into quotes (text, author, tags) values(%s, %s, %s)'
        li = [
            item['text'],
            item['author'],
            item['tags']
        ]
        self.cur.execute(ins, li)
        self.db.commit()
        return item

    def close_spider(self, spider):
        self.cur.close()
        self.db.close()


class QuotesMongoPipeline:
    def open_spider(self, spider):
        self.con = pymongo.MongoClient(host=MONGO_HOST, port=MONGO_PORT)
        self.db = self.con[MONGO_DB]
        self.set = self.db[MONGO_SET]

    def process_item(self, item, spider):
        d = dict(item)
        self.set.insert_one(d)
        return item
