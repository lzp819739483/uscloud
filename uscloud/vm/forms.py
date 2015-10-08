#!/usr/bin/env python
# encoding: utf-8
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from uscloud.template.models import Template


def template_list():
    return Template.query.all()

class AddVMForm(Form):
    name = StringField('vm_name', validators=[DataRequired()])
    temp_name = QuerySelectField(get_label='name', query_factory=template_list)
    submit = SubmitField('ADD')
