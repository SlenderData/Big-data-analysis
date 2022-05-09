# 我们查找文档中的 href="http://example.com/lacie"的节点元素<a>
from bs4 import BeautifulSoup

doc = '''
<html>
	<head>
		<title>The Dormouse's story</title>
	</head>
	<body> <a href="http://example.com/elsie">Elsie</a> <a href="http://example.com/lacie">Lacie</a> <a
			href="http://example.com/tillie">Tillie</a>
	</body>
</html>
'''


def myFilter(tag):
    print(tag.name)
    return (tag.name == "a" and tag.has_attr("href") and tag["href"] == "http://example.com/lacie")


soup = BeautifulSoup(doc, "lxml")
tag = soup.find_all(myFilter)
print(tag)
