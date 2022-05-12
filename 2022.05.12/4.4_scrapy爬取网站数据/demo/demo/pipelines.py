# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class BookPipeline(object):
    def open_spider(self, spider):
        print("opened")
        self.fobj = open("books.txt", "wt")
        self.opened = True

    def close_spider(self, spider):
        print("closed")
        if self.opened:
            self.fobj.close()

    def process_item(self, item, spider):
        try:
            # print(item["title"])
            self.fobj.write(item["title"] + "\n")
        except Exception as err:
            print(err)
        return item
