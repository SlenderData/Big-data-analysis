from scrapy import cmdline

cmdline.execute("scrapy crawl mySpider -s LOG_ENABLED=False".split())
