# 使用 xpath 查找 HTML 中的元素
from scrapy.selector import Selector

htmlText = '''
<html>
    <body>
        <bookstore>
            <book>
                <title lang="eng">Harry Potter</title>
                <price>29.99</price>
            </book>
            <book>
                <title lang="eng">Learning XML</title>
                <price>39.95</price>
            </book>
        </bookstore>
    </body>
</html>
'''
selector = Selector(text=htmlText)
print(type(selector));
print(selector)
s = selector.xpath("//title")
print(type(s))
print(s)
