#!/usr/bin/env python
# encoding: utf-8

"""
@author: li
@software: PyCharm
@file: views
@time: 16/09/15 7:38
"""

from flask import Blueprint, request, render_template
from .models import Host
from .forms import AddHostForm

host = Blueprint('host', __name__, url_prefix='/hosts')

@host.route('/', methods=['GET', 'POST'])
def index():
    form = AddHostForm()
    if request.method == 'GET':
        host_list = Host.query.all()
        return render_template('host/index.html', host_list=host_list, form=form)
    else:
        return 'hello world'

