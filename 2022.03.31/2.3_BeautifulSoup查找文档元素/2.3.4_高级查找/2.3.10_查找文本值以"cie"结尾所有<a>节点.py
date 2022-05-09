# 通过函数查找可以查找到一些复杂的节点元素
# 查找文本值以"cie"结尾所有<a>节点
from bs4 import BeautifulSoup

doc = '''
<html>
	<head>
		<title>The Dormouse's story</title>
	</head>
	<body> <a href="http://example.com/elsie">Elsie</a> <a href="http://example.com/lacie">Lacie</a> <a
			href="http://example.com/tillie">Tillie</a> <a href="http://example.com/tilcie">Tilcie</a>
	</body>
</html>
'''


def endsWith(s, t):
    if len(s) >= len(t):
        return s[len(s) - len(t):] == t
    return False


def myFilter(tag):
    return (tag.name == "a" and endsWith(tag.text, "cie"))


soup = BeautifulSoup(doc, "lxml")
tags = soup.find_all(myFilter)
for tag in tags:
    print(tag)
