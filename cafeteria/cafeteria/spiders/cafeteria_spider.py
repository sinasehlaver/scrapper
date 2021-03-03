from scrapy import Spider
from scrapy.selector import Selector
from datetime import datetime, timedelta

from cafeteria.items import CafeteriaItem, MenuItem

class CafeteriaSpider(Spider):
    date = datetime.now()
    date_str = str(date.day) + "-" + str(date.month) + "-" + str(date.year)
    name = "cafeteria"
    allowed_domains = ["kafeterya.metu.edu.tr"]
    start_urls = [
        "https://kafeterya.metu.edu.tr/tarih/"+date_str,
    ]

    def parse(self, response):
        date = datetime.now()
        date_str = str(date.day) + "-" + str(date.month) + "-" + str(date.year)
        selector = Selector(response)
        items = selector.xpath('//div[@class="yemek-listesi"]')

        for item in items:
            meal_time = item.xpath('h3/text()').extract_first()
            #print(meal_time)
            menu = CafeteriaItem()
            menu['meal_time'] = meal_time
            menu['date'] = date_str

            menu_items = []

            row = item.xpath('div[@class="yemek"]/p/text()').extract()

            for elem in row:
                elem_str = str(elem).strip()
                if elem_str != "*":
                    menu_item = MenuItem()
                    menu_item['name'] = elem_str
                    menu_items.append(menu_item)
                    #print(elem_str)

            menu['menu_items'] = menu_items

            yield menu

