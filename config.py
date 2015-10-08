import os

_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = False

# sql config
SQLALCHEMY_ECHO = True
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'app.db')

# wtf config
SECRET_KEY = 'nicainicainicaicaicai2015!@#'

MAIL_SERVER = 'smtp.126.com'
MAIL_PORT = 587
MAIL_USE_SSL = True
MAIL_USERNAME = os.getenv('U_MAIL_USERNAME')
MAIL_PASSWORD = os.getenv('U_MAIL_PASSWORD')
FLASKY_MAIL_SUBJECT_PREFIX = '[uscloud]'
FLASKY_MAIL_SENDER = 'lizhengpeng1133@126.com'
