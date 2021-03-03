# -*- coding: utf-8 -*-
from scrapy.item import Item, Field


class MenuItem(Item):
	name = Field()
	photo = Field()

class CafeteriaItem(Item):
    menu_items = Field()
    meal_time = Field()
    date = Field()
