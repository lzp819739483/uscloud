#!/usr/bin/env python
# encoding: utf-8
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired


class AddHostForm(Form):
    ip = StringField('IP', validators=[DataRequired()])
    name = StringField('NAME', validators=[DataRequired()])
    status_code = IntegerField('Status')
    submit = SubmitField('ADD')
