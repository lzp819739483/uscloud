#!/usr/bin/env python
# encoding: utf-8
from uscloud import db

class Image(db.Model):
    __tablename__ = 'images'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    path = db.Column(db.String(128), nullable=False)
    templates = db.relationship('Template', backref='image', lazy='dynamic')
