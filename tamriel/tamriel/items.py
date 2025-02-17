# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Field, Item


class TamrielItem(Item):
    # define the fields for your item here like:
    name = Field()
    price = Field()
    level = Field()
    trader_name = Field()
    quality = Field()
    location = Field()
    item_count = Field()
    entry_count = Field()

