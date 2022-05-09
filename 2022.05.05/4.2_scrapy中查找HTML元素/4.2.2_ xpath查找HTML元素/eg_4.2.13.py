# 搜索后面的兄弟节点
from scrapy.selector import Selector

htmlText = "<a>A1</a><b>B1</b><c>C1</c><d>D<e>E</e></d><b>B2</b><c>C2</c>"
selector = Selector(text=htmlText)
s = selector.xpath("//a/following-sibling::*")
print(s.extract())
s = selector.xpath("//a/following-sibling::*[position()=1]")
print(s.extract())
s = selector.xpath("//b[position()=1]/following-sibling::*")
print(s.extract())
s = selector.xpath("//b[position()=1]/following-sibling::*[position()=1]")
print(s.extract())
