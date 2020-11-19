# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymongo
import scrapy
from scrapy.utils.project import get_project_settings
settings = get_project_settings()
from scrapy.exceptions import DropItem


class WebPipeline(object):
    def __init__(self):
        connection = pymongo.MongoClient("mongodb+srv://abepro:abepro@cluster0.0qzk3.mongodb.net/work?retryWrites=true&w=majority")
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]

    def process_item(self, item, spider):
        for data in item:
            if not data:
                raise DropItem("Missing data!")
        self.collection.update({'_id' : item['_id']}, dict(item), upsert=True)
        return item

