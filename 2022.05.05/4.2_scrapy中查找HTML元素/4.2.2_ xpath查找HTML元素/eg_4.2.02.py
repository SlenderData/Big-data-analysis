# "//"与"/"的使用
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
# selector.xpath("//bookstore/book") 搜索<bookstore>下一级的<book>元素，找到 2 个；
# selector.xpath("//body/book") 搜索<body>下一级的<book>元素，结果为空；
# selector.xpath("//body//book") 搜索<body>下<book>元素，找到 2 个；
# selector.xpath("/body//book") 搜索文档下一级的<body>下的<book>元素，找结果为空，因为文档的下一级是<html>元素，不是<body>元素；
# selector.xpath("/html/body//book")或者 selector.xpath("/html//book") 搜索<book>元素，找到 2 个；
# selector.xpah("//book/title") 搜索文档中所有<book>下一级的<title>元素，找到 2 个，结果与 selector.xpah("//title")、selector.xpath("//bookstore//title")一样；
# selector.xpath("//book//price")与 selector.xpath("//price")结果一样，都是找到 2 个<price>元素；
print(type(selector));
print(selector)
s = selector.xpath("//title")
print(type(s))
print(s)
