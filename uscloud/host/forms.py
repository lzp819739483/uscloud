#!/usr/bin/env python
# encoding: utf-8
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired, AnyOf


class AddHostForm(Form):
    ip = StringField('IP', validators=[DataRequired()])
    name = StringField('NAME', validators=[DataRequired()])
    # status_code = IntegerField('Status', validators=[AnyOf(0, 1)])
    # status_code = SelectField('Status', choices=[('OK', 'ok'), ('Error', 'error')])
    submit = SubmitField('ADD')
