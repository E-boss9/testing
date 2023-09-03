import flask, os
from flask import sessions
import tempfile
from flask import session

app = flask.Flask(__name__)

# app.config["SESSION_FILE_DIR"] = '/templates'
# app.config["SESSION_PERMANENT"] = False
# app.config["SESSION_TYPE"] = "filesystem"

app.config["SECRET_KEY"] = 'something uniqe and secret'

for key, value in app.config.items():
    print(f"{key}: {value}")

@app.route("/")
def home():
    print(flask.session)
    session['tst'] = 'done'
    return flask.render_template("website.html")

@app.route("/page2")
def page2():
    return flask.render_template("page_2.html")

@app.route("/<string:name>")
def name(name):
    return f"hello {name}"

app.run("0.0.0.0")