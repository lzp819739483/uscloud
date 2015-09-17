#!/usr/bin/env python
# encoding: utf-8

"""
@author: li
@software: PyCharm
@file: views
@time: 16/09/15 7:38
"""

from flask import Blueprint

host = Blueprint('host', __name__, url_prefix='/')

@host.route('/')
def index():
    return 'hello uscloud'

