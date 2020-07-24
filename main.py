import api
from data import db_session
from flask import Flask, render_template

app = Flask(__name__)


@app.errorhandler(404)
def error_handler(error):
    return render_template("error_handler.html", message="Страница не найдена.")


@app.route("/")
def index():
    return render_template("base.html")


if __name__ == "__main__":
    db_session.global_init("db/database.sqlite")
    app.register_blueprint(api.api)
    app.run(host="127.0.0.1", port=8080)

