#!/usr/bin/env python
# encoding: utf-8
from flask import Blueprint, render_template, redirect, url_for, flash
from flask.ext.login import login_required

from uscloud.decorators import admin_required
from uscloud import db
from .models import Image
from .forms import AddImageForm

image = Blueprint('image', __name__, url_prefix='/image')

@image.route('/', methods=['GET', 'POST'])
@login_required
@admin_required
def index():
    form = AddImageForm()
    image_list = Image.query.all()
    if form.validate_on_submit():
        image_instance = Image(name=form.name.data, path=form.path.data)
        db.session.add(image_instance)
        db.session.commit()
        return redirect(url_for('image.index'))
    return render_template('image/index.html', form=form, image_list=image_list)

@image.route('/<int:image_id>/delete')
@login_required
@admin_required
def delete_image(image_id):
    image_instance = Image.query.filter(Image.id == image_id).first()
    if image_instance:
        db.session.delete(image_instance)
        db.session.commit()
    return redirect(url_for('image.index'))