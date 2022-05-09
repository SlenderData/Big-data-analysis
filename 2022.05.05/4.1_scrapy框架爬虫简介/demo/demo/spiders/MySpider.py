import scrapy


class MySpider(scrapy.Spider):
    name = "mySpider"

    def start_requests(self):
        url = 'http://127.0.0.1:5000'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        print(response.url)
        data = response.body.decode()
        print(data)
