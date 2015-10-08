#!/usr/bin/env python
# encoding: utf-8
from flask import Blueprint, render_template, redirect, request, url_for, flash
from flask.ext.login import login_required, login_user, logout_user, current_user
from .forms import LoginForm, RegistrationForm
from ..user.models import User
from uscloud import db
from uscloud.email import send_email


frontend = Blueprint('frontend', __name__)


@frontend.route('/', methods=['GET'])
def index():
    return redirect(url_for('vm.index'))


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
        db.session.commit()
        token = user.generate_confirmation_token()
        print "hello"+'  '+token
        send_email(user.email, 'Confirm Your Account', 'frontend/email/confirm', user=user, token=token)
        print "hello"+'  '+user.email
        flash('A confirmation email has been sent to you by email.')
        return redirect(url_for('frontend.login'))
    return render_template('frontend/register.html', form=form)

@frontend.route('/confirm/<token>')
@login_required
def confirm(token):
    if current_user.confirmed:
        return redirect(url_for('frontend.index'))
    if current_user.confirm(token):
        flash('You have confirmed your account. Thanks!')
    else:
        flash('The confirmation link is invalid or has expired.')
    return redirect(url_for('frontend.index'))

@frontend.before_app_request
def before_request():
    if current_user.is_authenticated \
            and not current_user.confirmed \
            and request.endpoint[:9] != 'frontend.' \
            and request.endpoint != 'static':
        return redirect(url_for('frontend.unconfirmed'))

@frontend.route('/unconfirmed')
@login_required
def unconfirmed():
    if current_user.is_anonymous or current_user.confirmed:
        return redirect(url_for('frontend.index'))
    return render_template('frontend/unconfirmed.html')

@frontend.route('/confirm')
@login_required
def resend_confirmation():
    token = current_user.generate_confirmation_token()
    send_email(current_user.email, 'Confirm Your Account', 'frontend/email/confirm', user=current_user, token=token)
    flash('A new confirmation email has been sent to you by email.')
    return redirect(url_for('frontend.index'))

