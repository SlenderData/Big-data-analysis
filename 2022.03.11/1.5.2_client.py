import urllib.parse
import urllib.request

url = "http://127.0.0.1:5000"
try:
    html = urllib.request.urlopen(url)
    html = html.read()
    fileName = html.decode()
    print("准备下载:" + fileName)
    urllib.request.urlretrieve(url + "?fileName=" + urllib.parse.quote(fileName), "download" + fileName)
    print("下载完毕")
except Exception as err:
    print(err)
