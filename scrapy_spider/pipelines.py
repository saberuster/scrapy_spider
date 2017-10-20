# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import logging

class ScrapySpiderPipeline(object):
    def process_item(self, item, spider):
        return item

class SaveAsJsonLinePipeline(object):

    def open_spider(self, spider):
        self.file = open('scrapy_spider/files/save.jl','w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item
    
