import urllib.parse
import urllib.request

url = "http://127.0.0.1:5000"
note = "深圳依山傍海，气候宜人，实在是适合人类居住的绝佳地。这里四季如春，干净整洁，比邻香港，拥有着丰富的自然景观和人文气息。匆匆过客注意到的也许只有它的时尚繁华，忙碌的暂居者也可能对它有着不识城市真面目之感。只有世代在此生活的老深圳人，才默默的看着它从贫穷走向富饶经历了怎样的艰辛。"
try:
    province = urllib.parse.quote("广东")
    city = urllib.parse.quote("深圳")
    note = "note=" + urllib.parse.quote(note)
    param = "province=" + province + "&city=" + city
    html = urllib.request.urlopen("http://127.0.0.1:5000?" + param, data=note.encode())
    html = html.read()
    html = html.decode()
    print(html)
except Exception as err:
    print(err)
