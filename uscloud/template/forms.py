#!/usr/bin/env python
# encoding: utf-8
from flask.ext.wtf import Form
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from uscloud.image.models import Image


def enabled_images():
    return Image.query.all()


class AddTempForm(Form):
    name = StringField('name', validators=[DataRequired()])
    cpu = IntegerField('cpu', validators=[DataRequired()])
    mem = IntegerField('memroy', validators=[DataRequired()])
    image_name = QuerySelectField(get_label='name', query_factory=enabled_images, validators=[DataRequired()])
    submit = SubmitField('ADD')
