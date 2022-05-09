# 使用"."进行 xpath 连续调用
from scrapy.selector import Selector

htmlText = '''
<html>
    <body>
        <bookstore>
            <title>books</title>
            <book>
                <title>Novel</title>
                <title lang="eng">Harry Potter</title>
                <price>29.99</price>
            </book>
            <book>
                <title>TextBook</title>
                <title lang="eng">Learning XML</title>
                <price>39.95</price>
            </book>
        </bookstore>
    </body>
</html>
'''
selector = Selector(text=htmlText)
s = selector.xpath("//book").xpath("./title")
for e in s:
    print(e)
