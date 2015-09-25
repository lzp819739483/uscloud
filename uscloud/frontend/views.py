#!/usr/bin/env python
# encoding: utf-8
from flask import Blueprint, render_template, redirect, request, url_for, flash
from flask.ext.login import login_required, login_user, logout_user

from .forms import LoginForm, RegistrationForm
from ..user.models import User
from uscloud import db


frontend = Blueprint('frontend', __name__)


@frontend.route('/', methods=['GET'])
def index():
    return redirect(url_for('host.index'))


@frontend.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, remember=form.remeber_me.data)
            return redirect(request.args.get('next') or url_for('host.index'))
        flash('Invalid username or password')
    return render_template('frontend/login.html', form=form)


@frontend.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have logout')
    return redirect(url_for('frontend.login'))

@frontend.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(name=form.name.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        # db.session.commit()
        flash('You can now login.')
        return redirect(url_for('frontend.login'))
    return render_template('frontend/register.html', form=form)


