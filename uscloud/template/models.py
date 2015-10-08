#!/usr/bin/env python
# encoding: utf-8
from uscloud import db


class Template(db.Model):
    __tablename__ = 'template'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    cpu = db.Column(db.SmallInteger)
    mem = db.Column(db.Integer)
    image_id = db.Column(db.Integer, db.ForeignKey('images.id'), nullable=False)
    vms = db.relationship('VM', backref='template', lazy='dynamic')
