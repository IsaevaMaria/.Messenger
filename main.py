import os
import api
from data.forms import *
from data import db_session
from flask import Flask, render_template

app = Flask(__name__)


@app.errorhandler(404)
def error_handler(error):
    return render_template("error_handler.html", message="Страница не найдена.")


@app.route("/")
def index():
    return render_template("base.html")


@app.route("/registration", methods=('GET', 'POST'))
def registration():
    session = db_session.create_session()
    form = RegistrationForm()
    if form.validate_on_submit():
        pass  # TODO
    return render_template("registration.html", form=form)


if __name__ == "__main__":
    db_session.global_init("db/database.sqlite")
    app.register_blueprint(api.api)
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
