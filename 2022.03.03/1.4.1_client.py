import urllib.parse
import urllib.request

url = "http://127.0.0.1:5000"
try:
    province = urllib.parse.quote("广东")
    city = urllib.parse.quote("深圳")
    data = "province=" + province + "&city=" + city
    data = data.encode()
    html = urllib.request.urlopen("http://127.0.0.1:5000", data=data)
    html = html.read()
    html = html.decode()
    print(html)
except Exception as err:
    print(err)
