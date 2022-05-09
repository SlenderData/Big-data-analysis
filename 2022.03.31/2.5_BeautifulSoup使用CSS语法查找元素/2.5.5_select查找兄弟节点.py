# 查找兄弟节点
from bs4 import BeautifulSoup

doc = "<body>demo<div>A</div><b>X</b><p>B</p><span><p>C</p></span><p>D</p></div></body>"
soup = BeautifulSoup(doc, "lxml")
print(soup.prettify())
tags = soup.select("div ~ p")
for tag in tags:
    print(tag)
print()
tags = soup.select("div + p")
for tag in tags:
    print(tag)
