# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class BiqukanprojectItem(scrapy.Item):
    url = scrapy.Field()
    title_novel = scrapy.Field()
    title_chapter = scrapy.Field()
    content = scrapy.Field()

