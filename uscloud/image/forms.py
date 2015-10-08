#!/usr/bin/env python
# encoding: utf-8
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class AddImageForm(Form):
    name = StringField('image_name', validators=[DataRequired()])
    path = StringField('path', validators=[DataRequired()])
    submit = SubmitField('ADD')

