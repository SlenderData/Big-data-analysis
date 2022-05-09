import urllib.request
import os

url = "http://127.0.0.1:5000/upload"
fileName = input("Enter the file:")
if os.path.exists(fileName):
    fobj = open(fileName, "rb")
    data = fobj.read()
    fobj.close()
    p = fileName.rfind("\\")
    fileName = fileName[p + 1:]
    print("准备上传:" + fileName)
    headers = {'countent-type': 'application/octet-stream'}
    purl = url + "?fileName=" + urllib.parse.quote(fileName)
    req = urllib.request.Request(purl, data, headers)
    msg = urllib.request.urlopen(req)
    msg = msg.read().decode()
    if msg == "OK":
        print("成功上传:", len(data), "字节")
    else:
        print(msg)
else:
    print("文件不存在!")
