#!/usr/bin/env python
# encoding: utf-8
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Regexp, Email

class AddUserForm(Form):
    name = StringField('NAME', validators=[DataRequired(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                                                                 'Username must have only letters,'
                                                                                 'numbers, dots or underscores')])
    email = StringField('Emali', validators=[DataRequired(), Length(1, 64), Email()])
    password = StringField('Password', validators=[DataRequired()])
    role = SelectField('role', choices=[('0', 'Admin'), ('1', 'Normal')])
    submit = SubmitField('ADD')
