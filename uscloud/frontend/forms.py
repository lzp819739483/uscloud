#!/usr/bin/env python
# encoding: utf-8
from flask.ext.wtf import Form
from wtforms import SubmitField, StringField, BooleanField
from wtforms.validators import Length, Email, DataRequired


class LoginForm(Form):
    email = StringField('email', validators=[DataRequired(), Length(1, 64), Email()])
    password = StringField('password', validators=[DataRequired()])
    remeber_me = BooleanField('Keep me login in')
    submit = SubmitField('Log in')
