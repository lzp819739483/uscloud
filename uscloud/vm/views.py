#!/usr/bin/env python
# encoding: utf-8
from flask import Blueprint, render_template, redirect, url_for
from flask.ext.login import login_required, current_user

from uscloud import db
from .models import VM
from .forms import AddVMForm

vm = Blueprint('vm', __name__, url_prefix='/vm')


@vm.route('/', methods=['GET', 'POST'])
@login_required
def index():
    form = AddVMForm()
    vm_list = VM.query.filter_by(user_id=current_user.id)
    if form.validate_on_submit():
        vm_instance = VM(name=form.name.data, template_id=form.temp_name.data.id, user_id=current_user.id)
        db.session.add(vm_instance)
        db.session.commit()
        return redirect(url_for('vm.index'))
    return render_template('vm/index.html', vm_list=vm_list, form=form)
