import flask

app = flask.Flask(__name__)


@app.route("/")
def index():
    try:
        province = flask.request.args.get("province") if "province" in flask.request.args else ""
        city = flask.request.args.get("city") if "city" in flask.request.args else ""
        return province + "," + city
    except Exception as err:
        return str(err)


if __name__ == "__main__":
    app.run()
