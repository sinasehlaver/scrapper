from scrapy import Spider
from scrapy.selector import Selector

from tamriel.items import TamrielItem

class TamrielSpider(Spider):
    name = "tamriel"
    allowed_domains = ["tamrieltradecentre.com"]
    start_urls = [
        "https://eu.tamrieltradecentre.com/pc/Trade/SearchResult?ItemID=6132&SortBy=LastSeen&Order=asc",
    ]

    def parse(self, response):

        selector = Selector(response)
        items = selector.xpath('//tr[@class="cursor-pointer"]')
        #print(response.css('tr.cursor-pointer').extract_first())
        # div[@class="col-md-6 popular-item-row form-group
        # div/div/div/text()
        # //*[@id="search-result-view"]/div[1]/div/table/tbody/tr[1]/td[1]/div[1]

        for item in items:
            row = item.xpath('td/div/text()').extract()
            for tr in row:
                print(str(tr).strip())
