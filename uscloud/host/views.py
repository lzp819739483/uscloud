#!/usr/bin/env python
# encoding: utf-8

"""
@author: li
@software: PyCharm
@file: views
@time: 16/09/15 7:38
"""
import libvirt
from flask import Blueprint, render_template, redirect, url_for, flash
from flask.ext.login import login_required

from .models import Host
from .forms import AddHostForm
from .. import db
from ..decorators import admin_required

host = Blueprint('host', __name__, url_prefix='/hosts')


@host.route('/', methods=['GET', 'POST'])
@login_required
@admin_required
def index():
    form = AddHostForm()
    host_list = Host.query.all()
    if form.validate_on_submit():
        host_instance = Host(ip=form.ip.data, name=form.name.data)
        db.session.add(host_instance)
        db.session.commit()
        return redirect(url_for('host.index'))
    return render_template('host/index.html', host_list=host_list, form=form)


@host.route('/<int:host_id>/delete', methods=['GET', 'POST'])
@login_required
@admin_required
def delete_host(host_id):
    host_instance = Host.query.filter(Host.id == host_id).first()
    if host_instance:
        # myTODO
        db.session.delete(host_instance)
        db.session.commit()
    return redirect(url_for('host.index'))


@host.route('/<int:host_id>/validate', methods=['GET', 'POST'])
@login_required
@admin_required
def validate_host(host_id):
    host_instance = Host.query.filter(Host.id == host_id).first()
    if host_instance:
        host_uri = 'qemu+ssh://root@'+host_instance.ip+'/system'
        try:
            host_conn = libvirt.open(host_uri)
            if host_conn.getHostname() == host_instance.name:
                host_instance.status_code = 0
                db.session.add(host_instance)
                db.session.commit()
                flash(host_instance.name+' is OK!!!')
            else:
                flash(host_instance.name+"'s name is error, please check it!!!")
        except:
            flash(host_instance.name+' is Not OK, please check it!!!')
    return redirect(url_for('host.index'))
