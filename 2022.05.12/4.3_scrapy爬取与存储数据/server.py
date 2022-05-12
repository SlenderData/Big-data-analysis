import flask

app = flask.Flask(__name__)


@app.route("/")
def index():
    html = """
    <books>
        <book>
            <title>Python 程序设计</title>
            <author>James</author>
            <publisher>清华大学出版社</publisher>
        </book>
        <book>
            <title>Java 程序设计</title>
            <author>Robert</author>
            <publisher>人民邮电出版社</publisher>
        </book>
        <book>
            <title>MySQL 数据库</title>
            <author>Steven</author>
            <publisher>高等教育出版社</publisher>
        </book>
    </books>
    """
    return html


if __name__ == "__main__":
    app.run()
