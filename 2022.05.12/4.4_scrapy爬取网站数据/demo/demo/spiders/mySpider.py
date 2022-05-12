import scrapy
from demo.items import BookItem


class MySpider(scrapy.Spider):
    name = "mySpider"
    start_urls = ['http://127.0.0.1:5000']

    def parse(self, response):
        try:
            print(response.url)
            data = response.body.decode()
            selector = scrapy.Selector(text=data)
            title = selector.xpath("//h3/text()").extract_first()
            print(title)
            item = BookItem()
            item["title"] = title
            yield item
            links = selector.xpath("//a/@href").extract()
            for link in links:
                url = response.urljoin(link)
                yield scrapy.Request(url=url, callback=self.parse)
        except Exception as err:
            print(err)
