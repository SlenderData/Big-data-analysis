import flask

app = flask.Flask(__name__)


@app.route("/upload", methods=["POST"])
def uploadFile():
    msg = ""
    try:
        if "fileName" in flask.request.values:
            fileName = flask.request.values.get("fileName")
            data = flask.request.get_data()
            fobj = open("upload" + fileName, "wb")
            fobj.write(data)
            fobj.close()
            msg = "OK"
        else:
            msg = "没有按要求上传文件"
    except Exception as err:
        print(err)
        msg = str(err)
    return msg


if __name__ == "__main__":
    app.run()
