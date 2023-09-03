import flask


app = flask.Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def hello():
    name = flask.request.args.get("name")
    # if name:
        # return flask.redirect(flask.url_for('hello_someone', name=name))
    return flask.render_template("index.html", name=name)

@app.route("/page/<name>")
def hello_someone(name=None):
    return f"hello {name}"



app.run()

