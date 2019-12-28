from flask import render_template, request, url_for, flash
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from werkzeug.utils import redirect

from app.forms import Form, LoginForm, RegistrationForm
from app.generate import Generate
from app.models import User
from app import app, db


@app.route("/home", methods=['GET', 'POST'])
def hello():
    form = Form()
    tes = Generate(form.count_of_symbol.data)
    password = None
    if request.method == "POST":
        password = tes.generate(
                            form.up_and_lw.data,
                            form.digit.data,
                            form.special_symbol.data)
    password_entropy = tes.password_entropy()
    return render_template("home.html", form=form, password=password, password_entropy=password_entropy)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('hello'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('hello')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('hello'))


@app.route('/pass_list')
@login_required
def get_all_password():
    return render_template('all_password.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)
