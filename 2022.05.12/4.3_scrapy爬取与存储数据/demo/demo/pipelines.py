# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class BookPipeline(object):
    count = 0

    def process_item(self, item, spider):
        BookPipeline.count += 1
        try:
            if BookPipeline.count == 1:
                fobj = open("../../books.txt", "wt")
            else:
                fobj = open("../../books.txt", "at")
            print(item["title"], item["author"], item["publisher"])
            fobj.write(item["title"] + "," + item["author"] + "," + item["publisher"] + "\n")
            fobj.close()
        except Exception as err:
            print(err)
        return item
