#!/usr/bin/env python
# encoding: utf-8
from flask import Blueprint, render_template, redirect, url_for
from flask.ext.login import login_required

from uscloud.decorators import admin_required
from uscloud import db
from .models import Template
from .forms import AddTempForm

template = Blueprint('template', __name__, url_prefix='/template')


@template.route('/', methods=['GET', 'POST'])
@login_required
@admin_required
def index():
    form = AddTempForm()
    template_list = Template.query.all()
    if form.validate_on_submit():
        template_instance = Template(name=form.name.data, cpu=form.cpu.data,
                                     mem=form.mem.data, image_id=form.image_name.data.id)
        print template_instance
        db.session.add(template_instance)
        db.session.commit()
        return redirect(url_for('template.index'))
    return render_template('template/index.html', template_list=template_list, form=form)

@template.route('/<int:temp_id>/delete')
@login_required
@admin_required
def delete_temp(temp_id):
    temp_instance = Template.query.filter(Template.id == temp_id).first()
    if temp_instance:
        db.session.delete(temp_instance)
        db.session.commit()
    return redirect(url_for('template.index'))