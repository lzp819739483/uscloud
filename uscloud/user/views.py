#!/usr/bin/env python
# encoding: utf-8
from flask import Blueprint, request, render_template, redirect, url_for
from flask.ext.login import login_required, current_user

from ..decorators import admin_required
from .forms import AddUserForm
from .models import User
from .. import db

user = Blueprint('user', __name__, url_prefix='/user')

@user.route('/', methods=['GET', 'POST'])
@login_required
@admin_required
def index():
    form = AddUserForm()
    user_list = User.query.all()
    if form.validate_on_submit():
        user_instance = User(name=form.name.data, email=form.email.data, role=form.role.data,
                             password=form.password.data)
        db.session.add(user_instance)
        db.session.commit()
        return redirect(url_for('user.index'))
    return render_template('user/index.html', user_list=user_list, form=form)

@user.route('/<int:user_id>/delete')
@login_required
@admin_required
def delete_user(user_id):
    user_instance = User.query.filter(User.id == user_id).first()
    if user_instance:
        db.session.delete(user_instance)
        db.session.commit()
    return redirect(url_for('user.index'))
