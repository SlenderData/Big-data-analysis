# 查找HTML文档中所有<p>下面的<a>的链接
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
			<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
			<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
			<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
			and they lived at the bottom of a well.
		</p>
		<p class="story">...</p>
	</body>
</html>
'''
soup = BeautifulSoup(doc, "lxml")
tags = soup.select("p[class='story'] a")
for tag in tags:
    print(tag["href"])
