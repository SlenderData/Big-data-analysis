# 使用递归
from bs4 import BeautifulSoup
import urllib.request


def spider(url):
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
            # print(url)
            spider(url)
    except Exception as err:
        print(err)


start_url = "http://127.0.0.1:5000"
spider(start_url)
print("The End")
