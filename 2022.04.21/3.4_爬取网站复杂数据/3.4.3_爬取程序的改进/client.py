from bs4 import BeautifulSoup
import urllib.request
import threading


def download(url, fileName):
    try:
        # 设置下载时间最长 100 秒
        data = urllib.request.urlopen(url, timeout=100)
        data = data.read()
        fobj = open("downloaded " + fileName, "wb")
        fobj.write(data)
        fobj.close()
        print("downloaded ", fileName)
    except Exception as err:
        print(err)


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
            divs = soup.select("div")
            imgs = soup.select("img")
            if len(divs) > 0 and len(imgs) > 0:
                note = divs[0].text
                print(note)
                url = start_url + "/" + imgs[0]["src"]
                # 启动一个下载线程下载图像
                T = threading.Thread(target=download, args=(url, imgs[0]["src"]))
                T.setDaemon(False)
                T.start()
                threads.append(T)
            for link in links:
                href = link["href"]
                url = start_url + "/" + href
                spider(url)
        except Exception as err:
            print(err)


start_url = "http://127.0.0.1:5000"
urls = []
threads = []
spider(start_url)
# 等待所有线程执行完毕
for t in threads:
    t.join()
print("The End")
