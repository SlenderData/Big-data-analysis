import scrapy
from demo.items import BookItem


class MySpider(scrapy.Spider):
    name = "mySpider"
    start_urls = ['http://127.0.0.1:5000']

    def parse(self, response):
        try:
            data = response.body.decode()
            selector = scrapy.Selector(text=data)
            books = selector.xpath("//book")
            for book in books:
                item = BookItem()
                item["title"] = book.xpath("./title/text()").extract_first()
                item["author"] = book.xpath("./author/text()").extract_first()
                item["publisher"] = book.xpath("./publisher/text()").extract_first()
                yield item
        except Exception as err:
            print(err)
