from data import db_session
from flask import Flask, render_template
import os

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("base.html")

if __name__ == "__main__":
    db_session.global_init("db/database.sqlite")
    app.run(host="127.0.0.1", port=8080)
