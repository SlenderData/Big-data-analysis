# 获取<p>元素的所有子孙元素节点
from bs4 import BeautifulSoup

doc = '''
<html>
	<head>
		<title>The Dormouse's story</title>
	</head>
	<body>
		<p class="title"><b>The <i>Dormouse's</i> story</b> Once upon a time ...</p>
	</body>
</html>
'''
soup = BeautifulSoup(doc, "lxml")
tag = soup.find("p")
for x in tag.descendants:
    print(x)
