import os
import api
from data.forms import *
from sqlalchemy import or_
from data import db_session
from data.__all_models import *
from flask import Flask, render_template, redirect
from flask_login import login_user, logout_user, current_user, LoginManager, login_required

app = Flask(__name__)
app.config["SECRET_KEY"] = "messenger"
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return session.query(users.Users).get(user_id)


@app.errorhandler(401)
def unauthorized(error):
    return render_template('no_access.html'), 401


@app.errorhandler(404)
def error_handler(error):
    return render_template("error_handler.html", message="Страница не найдена."), 404


@app.route("/")
def index():
    return render_template("base.html", current_user=current_user)


@app.route("/registration", methods=('GET', 'POST'))
def registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        if form.password.data == "" or form.login.data == "" or form.confirm_password.data == ""\
                or form.nickname.data == "":
            return render_template("registration.html", form=form, message="Заполните все поля")
        if form.password.data != form.confirm_password.data:
            return render_template("registration.html", form=form, message="Пароли не совпадают.")
        new_user = users.Users()
        new_user.name = form.nickname.data
        new_user.set_password(form.password.data)
        new_user.email = form.login.data
        session.add(new_user)
        session.commit()
        login_user(new_user)
        return redirect("/")
    return render_template("registration.html", form=form, message="")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route("/login", methods=('GET', 'POST'))
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.password.data == "" or form.login.data == "":
            return render_template("login.html", form=form, message="Заполните все поля")
        user = session.query(users.Users).filter(users.Users.email == form.login.data).first()
        if user is None:
            return render_template("login.html", form=form, message="Пользователь не найден")
        if not user.check_password(form.password.data):
            return render_template("login.html", form=form, message="Неправильный пароль")
        login_user(user, remember=form.remember.data)
        return redirect("/")
    return render_template("login.html", form=form, message="")


@app.route("/friends")
@login_required
def friend():
    friends_list = session.query(friends.Friends).filter(
        or_(friends.Friends.id_first_user == current_user.id,
            friends.Friends.id_second_user == current_user.id)).all()
    friends_list = [pair.id_first_user if pair.id_first_user != current_user.id
                    else pair.id_second_user for pair in friends_list]
    friends_list = [session.query(users.Users).get(user) for user in friends_list]
    return render_template("friends.html", friends_list=friends_list)


if __name__ == "__main__":
    db_session.global_init("db/database.sqlite")
    session = db_session.create_session()
    app.register_blueprint(api.api)
    #  app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
    app.run(host="127.0.0.1", port=8080)
