# 不要尝试执行本程序
# 爬取目标网站已无法访问
import urllib.request
from bs4 import BeautifulSoup
import sqlite3
import json
import time


class MySpider:
    def openDB(self):
        self.con = sqlite3.connect("scenes.db")
        self.cursor = self.con.cursor()

    def initDB(self):
        try:
            self.cursor.execute("drop table scenes")
        except:
            pass
            self.cursor.execute(
                "create table scenes (sName varchar(256) primary key, sType varchar(1024), sSource  varchar(1024), sLevel varchar(256), sTime varchar(256), sHotel varchar(1024))")

    def closeDB(self):
        self.con.commit()
        self.con.close()

    def insertDB(self, sName, sType, sSource, sLevel, sTime, sHotel):
        try:
            self.con = sqlite3.connect("sences.db")
            self.cursor = self.con.cursor()
            sql = "insert into scenes (sName, sType, sSource, sLevel, sTime, sHotel) value (?, ?, ?, ?, ?, ?)"
            self.cursor.execute(sql, [sName, json.dumps(sType), json.dumps(sSource), sLevel, sTime, json.dumps(sHotel)])
        except:
            pass

    def spider(self, url):
        try:
            resp = urllib.request.urlopen(url)
            html = resp.read().decode()
            soup = BeautifulSoup(html, "lxml")
            divs = soup.find("div", attrs={"class": "sightlist"}).find_all("div", attrs={"class": "sightshow"})
            for div in divs:
                dd = div.find("div", attrs={"class": "sightdetail"})
                sName = dd.find("h4").find("a").text
                lis = dd.find("ul", attrs={"class": "sightbase"}).find_all("li")
                sType = []
                if len(lis) > 0:
                    for link in lis[0].find_all("a"):
                        sType.append(link.text)
                sSource = []
                if len(lis) > 1:
                    for link in lis[1].find_all("a"):
                        sSource.append(link.text)
                if len(lis) > 2:
                    sLevel = lis[2].find("span").find("a").text
                    sTime = lis[2].find("a", recursive=False).text
                else:
                    sLevel = ""
                    sTime = ""
                lis = dd.find("ul", attrs={"class": "sighthotel"}).find_all("li")
                sHotel = []
                for li in lis:
                    h = {}
                    h["name"] = li.find("a").text
                    h["price"] = li.find("span").text
                    sHotel.append(h)
                self.insertDB(sName, sType, sSource, sLevel, sTime, sHotel)
                print(sName)
        except Exception as err:
            print(err)

    def showDB(self):
        # self.cursor.execute("select sName, sType, sSource, sLevel, sTime, sHotel from scenes")
        # self.cursor = self.con.cursor()
        self.cursor.execute("select sName, sType, sSource, sLevel, sTime, sHotel from scenes")
        rows = self.cursor.fetchall()
        no = 0
        for row in rows:
            no = no + 1
            print("No", no)
            print("名称：", row[0], "  时间：", row[4], "  级别：", row[3])
            sType = json.loads(row[1])
            print("类型：", end="")
            for t in sType:
                print(t, end="")
            print()
            sSource = json.loads(row[2])
            print("资源：", end="")
            for t in sSource:
                print(t, end="")
            print()
            print("酒店：")
            sHotel = json.loads(row[5])
            for h in sHotel:
                print(h["name"], h["price"])
            print()
        print("Total", len(rows))

    def getPageCount(self):
        count = 0
        try:
            resp = urllib.request.urlopen("http://scenic.cthy.com/scenicSearch/0-0-201-0-0-1.html")  # 该网址已无法访问
            html = resp.read().decode()
            soup = BeautifulSoup(html, "lxml")
            count = int(soup.find("ul", attrs={"id": "PagerList"}).find("li").find_all("span")[1].text)
        except Exception as err:
            print(err)
        return count

    def process(self):
        self.openDB()
        self.initDB()
        count = self.getPageCount()
        print("Total ", count, " pages")
        for p in range(1, count + 1):
            # time.sleep(4.0)
            url = "http://scenic.cthy.com/scenicSearch/0-0-201-0-0-" + str(p) + ".html"
            print("Page", p, " ", url)
            self.spider(url)
            self.showDB()
            self.closeDB()

    def show(self):
        self.openDB()
        self.showDB()
        self.closeDB()


spider = MySpider()
while True:
    print("1. 爬取")
    print("2. 显示")
    print("3. 退出")
    s = input("选择(1,2,3): ")
    if s == "1":
        spider.process()
    elif s == "2":
        spider.show()
    elif s == "3":
        break
