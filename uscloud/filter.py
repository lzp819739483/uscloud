#!/usr/bin/env python
# encoding: utf-8

def role_display(value):
    USER_ADMIN = 0
    USER_NORMAL = 1
    USER_TYPE = {USER_ADMIN: 'ADMIN', USER_NORMAL: 'NORMAL'}
    return USER_TYPE[value]


