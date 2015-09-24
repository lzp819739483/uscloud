#!/usr/bin/env python
# encoding: utf-8
from flask import Blueprint, request, render_template, redirect, url_for
from .models import User
# from .forms import AddHostForm
from .. import db

user = Blueprint('user', __name__, url_prefix='/user')
