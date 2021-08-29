# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import os

from itemadapter import ItemAdapter


class DaomuPipeline:
    def process_item(self, item, spider):
        directory = './Notes/{}'.format(item['homebook'])
        if not os.path.exists(directory):
            os.mkdir(directory)
        filename = './Notes/{}/{}.txt'.format(item['homebook'], item['excerpts'])
        with open(filename, 'w') as f:
            f.write(item['content'])
        return item

