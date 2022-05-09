# 查找子孙节点
from bs4 import BeautifulSoup

doc = "<div><p>A</p><span><p>B</p></span></div><div><p>C</p></div>"
soup = BeautifulSoup(doc, "lxml")
tags = soup.select("div p")
for tag in tags:
    print(tag)
