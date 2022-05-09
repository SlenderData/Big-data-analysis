# extract 与 extract_first 函数使用
from scrapy.selector import Selector

htmlText = '''
<html>
    <body>
        <bookstore>
            <book id="b1">
                <title lang="english">Harry Potter</title>
                <price>29.99</price>
            </book>
            <book id="b2">
                <title lang="chinese">学习 XML</title>
                <price>39.95</price>
            </book>
        </bookstore>
    </body>
</html>
'''
selector = Selector(text=htmlText)
s = selector.xpath("//book/price")
print(type(s), s)
s = selector.xpath("//book/price").extract()
print(type(s), s)
s = selector.xpath("//book/price").extract_first()
print(type(s), s)
