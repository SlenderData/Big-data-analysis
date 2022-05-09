# 改进深度优先客户端程序
# 使用递归
from bs4 import BeautifulSoup
import urllib.request


def spider(url):
    global urls
    if url not in urls:
        urls.append(url)
        try:
            data = urllib.request.urlopen(url)
            data = data.read()
            data = data.decode()
            soup = BeautifulSoup(data, "lxml")
            print(soup.find("h3").text)
            links = soup.select("a")
            for link in links:
                href = link["href"]
                url = start_url + "/" + href
                spider(url)
        except Exception as err:
            print(err)


start_url = "http://127.0.0.1:5000"
urls = []
spider(start_url)
print("The End")
