#!/usr/bin/env python
# encoding: utf-8
from werkzeug.security import generate_password_hash, check_password_hash
from .. import db

class User(db.Model):
    __tablename__ = 'users'

