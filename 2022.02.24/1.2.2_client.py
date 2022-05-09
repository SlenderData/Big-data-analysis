import urllib.request

url = "http://127.0.0.1:5000"
html = urllib.request.urlopen(url)
html = html.read()
html = html.decode()
print(html)
