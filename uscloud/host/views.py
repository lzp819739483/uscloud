#!/usr/bin/env python
# encoding: utf-8

"""
@author: li
@software: PyCharm
@file: views
@time: 16/09/15 7:38
"""

from flask import Blueprint, request, render_template, redirect, url_for
from flask.ext.login import login_required
from .models import Host
from .forms import AddHostForm
from .. import db

host = Blueprint('host', __name__, url_prefix='/hosts')


@host.route('/', methods=['GET', 'POST'])
# @login_required
def index():
    form = AddHostForm()
    if request.method == 'GET':
        host_list = Host.query.all()
        return render_template('host/index.html', host_list=host_list, form=form)
    else:
        if form.validate_on_submit():
            host_instance = Host(ip=form.ip.data, name=form.name.data)
            db.session.add(host_instance)
            db.session.commit()
        return redirect(url_for('host.index'))


@host.route('/<int:host_id>/delete', methods=['GET', 'POST'])
def delete_host(host_id):
    host_instance = Host.query.filter(Host.id == host_id).first()
    if host_instance:
        db.session.delete(host_instance)
        db.session.commit()
    return redirect(url_for('host.index'))
