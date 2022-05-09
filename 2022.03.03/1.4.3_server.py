import flask

app = flask.Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    try:
        province = flask.request.values.get("province") if "province" in flask.request.values else ""
        city = flask.request.values.get("city") if "city" in flask.request.values else ""
        note = flask.request.values.get("note") if "note" in flask.request.values else ""
        return province + "," + city + "\n" + note
    except Exception as err:
        return str(err)


if __name__ == "__main__":
    app.run()
