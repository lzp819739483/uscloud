#!/usr/bin/env python
# encoding: utf-8
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms import ValidationError

from uscloud.template.models import Template
from uscloud.vm.models import VM


def template_list():
    return Template.query.all()


class AddVMForm(Form):
    name = StringField('vm_name', validators=[DataRequired()])
    temp_name = QuerySelectField(get_label='name', query_factory=template_list, validators=[DataRequired()])
    submit = SubmitField('ADD')

    def validate_name(self, field):
        if VM.query.filter_by(name=field.data).first():
            raise ValidationError('vm name already in')
