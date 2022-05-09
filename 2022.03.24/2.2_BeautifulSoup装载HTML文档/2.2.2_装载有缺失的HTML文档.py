# BeautifulSoup装载有缺失的HTML文档
from bs4 import BeautifulSoup

doc = '''
<title>有缺失元素的 HTML 文档</title>
<div>
<A href='one.html'>one</a>
<p>
<a href='two.html'>two</a>
</DIV>
'''
soup = BeautifulSoup(doc, "lxml")
s = soup.prettify()
print(s)
