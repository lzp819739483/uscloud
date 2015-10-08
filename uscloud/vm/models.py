#!/usr/bin/env python
# encoding: utf-8
from datetime import datetime

from uscloud import db


class VM(db.Model):
    __tablename__ = 'vm'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    template_id = db.Column(db.Integer, db.ForeignKey('template.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.utcnow)
