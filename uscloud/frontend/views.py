#!/usr/bin/env python
# encoding: utf-8
from flask import Blueprint, render_template, redirect, request, url_for, flash
from flask.ext.login import login_required, login_user

from .forms import LoginForm
from ..user.models import User


frontend = Blueprint('frontend', __name__)

@frontend.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and User.verify_password(form.password.data):
            login_user(user, remember=form.remeber_me.data)
            return redirect(request.args.get('next') or url_for('host.index'))
        # flash('Invalid username or password')
    return render_template('frontend/login.html', form=form)
