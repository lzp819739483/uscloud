#!/usr/bin/env python
# encoding: utf-8

from uscloud import db

# Host status
HOST_OK = 0
HOST_ERROR = 1

HOST_STATUS = {
    HOST_OK: 'OK',
    HOST_ERROR: 'ERROR',
}


class Host(db.Model):
    __tablename__ = 'hosts'

    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(64), nullable=False, unique=True)
    name = db.Column(db.String(64), nullable=False)
    status_code = db.Column(db.SmallInteger, default=HOST_ERROR)

    def __repr__(self):
        return '<Host %r>' % self.name
