# 多个文本节点值
from scrapy.selector import Selector

htmlText = '''
<html>
    <body>
        <bookstore>
            <book id="b1">
                <title lang="english"><b>H</b>arry <b>P</b>otter</title>
                <price>29.99</price>
            </book>
        </bookstore>
    </body>
</html>

'''
selector = Selector(text=htmlText)
s = selector.xpath("//book/title/text()")
print(s)
print(s.extract())
for e in s:
    print(e.extract())
