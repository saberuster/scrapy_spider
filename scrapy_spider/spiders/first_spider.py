import scrapy
from scrapy_spider.items import FirstItem

class FirstSpider(scrapy.Spider):
    name = "first"
    start_urls = [
        "http://www.yw11.com/html/mi/3-6-1-1.htm"
    ]

    # def start_requests(self):
    #       url = "http://www.yw11.com/html/mi/3-{0}-{1}-1.htm"
    #       for page in range(500):
    #           for gender in range(1, 2):
    #               yield scrapy.Request(url=url.format(page, gender), callback=self.parse)

    def parse(self, response):
        for name in response.css(".listbox1_text ul li::text"):
            yield FirstItem(name=name.extract().strip())
