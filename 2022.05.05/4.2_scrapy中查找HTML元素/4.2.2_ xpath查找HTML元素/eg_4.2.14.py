# 搜索前面的兄弟节点
from scrapy.selector import Selector

htmlText = "<a>A1</a><b>B1</b><c>C1</c><d>D<e>E</e></d><b>B2</b><c>C2</c>"
selector = Selector(text=htmlText)
s = selector.xpath("//a/preceding-sibling::*")
print(s.extract())
s = selector.xpath("//b/preceding-sibling::*[position()=1]")
print(s.extract())
s = selector.xpath("//b[position()=2]/preceding-sibling::*")
print(s.extract())
s = selector.xpath("//b[position()=2]/preceding-sibling::*[position()=1]")
print(s.extract())
