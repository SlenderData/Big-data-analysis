import flask

app = flask.Flask(__name__)


@app.route("/", methods=["POST"])
def index():
    try:
        province = flask.request.form.get("province") if "province" in flask.request.form else ""
        city = flask.request.form.get("city") if "city" in flask.request.form else ""
        return province + "," + city
    except Exception as err:
        return str(err)


if __name__ == "__main__":
    app.run()
