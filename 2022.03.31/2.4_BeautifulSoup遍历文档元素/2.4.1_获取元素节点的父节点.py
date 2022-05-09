# 找出文档中<p class="title"><b>The Dormouse's story</b></p>的<b>元素节点的所有父节点的名称
from bs4 import BeautifulSoup

doc = '''
<html>
	<head>
		<title>The Dormouse's story</title>
	</head>
	<body>
		<p class="title"><b>The Dormouse's story</b></p>
		<p class="story">
			Once upon a time there were three little sisters; and their names were
			<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>, <a href="http://example.com/lacie"
				class="sister" id="link2">Lacie</a> and
			<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
			and they lived at the bottom of a well.
		</p>
		<p class="story">...</p>
	</body>
</html>
'''
soup = BeautifulSoup(doc, "lxml")
print(soup.name)
tag = soup.find("b")
while tag:
    print(tag.name)
    tag = tag.parent
