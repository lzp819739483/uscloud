from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bootstrap import Bootstrap
from flask.ext.login import LoginManager
from flask.ext.mail import Mail
from flask_debugtoolbar import DebugToolbarExtension

from .filter import *

app = Flask(__name__, instance_relative_config=True)

app.config.from_object('config')
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)

bootstrap = Bootstrap(app)

login_manager = LoginManager()
# comment because of "csrf token missing"
# login_manager.session_protection = 'strong'
login_manager.login_view = 'frontend.login'
login_manager.init_app(app)

mail = Mail(app)

toolbar = DebugToolbarExtension(app)

from uscloud.host.views import host as hostModule
app.register_blueprint(hostModule)

from uscloud.user.views import user as userModule
app.register_blueprint(userModule)

from uscloud.frontend.views import frontend as frontendModule
app.register_blueprint(frontendModule)

from uscloud.image.views import image as imageModule
app.register_blueprint(imageModule)

from uscloud.template.views import template as templateModule
app.register_blueprint(templateModule)

from uscloud.vm.views import vm as vmModule
app.register_blueprint(vmModule)

app.jinja_env.filters['role_display']=role_display
