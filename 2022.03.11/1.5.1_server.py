import flask
import os

app = flask.Flask(__name__)


@app.route("/")
def index():
    if "fileName" not in flask.request.values:
        return "图像.jpg"
    else:
        data = b""
        try:
            fileName = flask.request.values.get("fileName")
            if fileName != "" and os.path.exists(fileName):
                fobj = open(fileName, "rb")
                data = fobj.read()
                fobj.close()
        except Exception as err:
            data = str(err).encode()
        return data


if __name__ == "__main__":
    app.run()
