import os

_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = False

# sql config
SQLALCHEMY_ECHO = True
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'app.db')

# wtf config
SECRET_KEY = 'nicainicainicaicaicai2015!@#'
