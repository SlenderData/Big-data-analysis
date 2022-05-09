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
            divs = soup.select("div")
            imgs = soup.select("img")
            if len(divs) > 0 and len(imgs) > 0:
                print(divs[0].text)
                url = start_url + "/" + imgs[0]["src"]
                urllib.request.urlretrieve(url, "downloaded " + imgs[0]["src"])
                print("downloaded ", imgs[0]["src"])
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
