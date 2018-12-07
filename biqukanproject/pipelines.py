# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

class BiqukanprojectPipeline(object):
    def __init__(self):
        self.file = open('novel.json',"wb")
    def process_item(self, item, spider):
        self.file.write(bytes(str(item),encoding='utf-8'))
        return item
