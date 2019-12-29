from app import db, login
from flask_login import UserMixin
from passlib.hash import sha256_crypt


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    pas = db.relationship('Passwords', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = sha256_crypt.hash(password)

    def check_password(self, password):
        return sha256_crypt.verify(password, self.password_hash)


class Passwords(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(140))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Passwords {}>'.format(self.password)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
