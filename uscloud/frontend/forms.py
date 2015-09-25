#!/usr/bin/env python
# encoding: utf-8
from flask.ext.wtf import Form
from wtforms import SubmitField, StringField, BooleanField, PasswordField
from wtforms.validators import Length, Email, DataRequired, Regexp, EqualTo
from wtforms import ValidationError
from ..user.models import User


class LoginForm(Form):
    email = StringField('email', validators=[DataRequired(), Length(1, 64), Email()])
    password = StringField('password', validators=[DataRequired()])
    remeber_me = BooleanField('Keep me login in')
    submit = SubmitField('Log in')


class RegistrationForm(Form):
    name = StringField('name', validators=[DataRequired(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                                                                 'Usernames must have only letters,'
                                                                                 'numbers, dots or underscores')])
    email = StringField('email', validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField('password', validators=[DataRequired(), EqualTo('password2', 'Passwords must match.')])
    password2 = PasswordField('confirm password', validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered')

    def validate_name(self, field):
        if User.query.filter_by(name=field.data).first():
            raise ValidationError('Username already in use')
