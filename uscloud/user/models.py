#!/usr/bin/env python
# encoding: utf-8
from werkzeug.security import generate_password_hash, check_password_hash
from flask.ext.login import UserMixin
from uscloud import db, login_manager

# User role
USER_ADMIN = 0
USER_NORMAL = 1
USER_TYPE = {
    USER_ADMIN: 'ADMIN',
    USER_NORMAL: 'USER',
}


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True)
    email = db.Column(db.String(128), unique=True)
    role = db.Column(db.SmallInteger, default=USER_NORMAL)
    password_hash = db.Column(db.String(128), nullable=False)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


