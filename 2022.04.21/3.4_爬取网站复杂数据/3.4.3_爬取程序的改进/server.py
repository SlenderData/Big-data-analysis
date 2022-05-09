import flask
import os
import random
import time

app = flask.Flask(__name__)


def getFile(fileName):
    data = b""
    if os.path.exists(fileName):
        fobj = open(fileName, "rb")
        data = fobj.read()
        fobj.close()
        # 随机等待 1-10 秒
        time.sleep(random.randint(1, 10))
    return data


@app.route("/")
def index():
    return getFile("books.html")


@app.route("/<section>")
def process(section):
    data = ""
    if section != "":
        data = getFile(section)
    return data


if __name__ == "__main__":
    app.run()
