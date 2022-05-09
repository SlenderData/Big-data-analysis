# 改进深度优先客户端程序
# 使用栈
from bs4 import BeautifulSoup
import urllib.request


class Stack:
    def __init__(self):
        self.st = []

    def pop(self):
        return self.st.pop()

    def push(self, obj):
        self.st.append(obj)

    def empty(self):
        return len(self.st) == 0


def spider(url):
    global urls
    stack = Stack()
    stack.push(url)
    while not stack.empty():
        url = stack.pop()
        if url not in urls:
            urls.append(url)
            try:
                data = urllib.request.urlopen(url)
                data = data.read()
                data = data.decode()
                soup = BeautifulSoup(data, "lxml")
                print(soup.find("h3").text)
                links = soup.select("a")
                for i in range(len(links) - 1, -1, -1):
                    href = links[i]["href"]
                    url = start_url + "/" + href
                    stack.push(url)
            except Exception as err:
                print(err)


start_url = "http://127.0.0.1:5000"
urls = []
spider(start_url)
print("The End")
