#  使用"*"代表任何 element 元素
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
s = selector.xpath("//bookstore/*/title")
print(s.extract())
