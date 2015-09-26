from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bootstrap import Bootstrap
from flask.ext.login import LoginManager
from flask.ext.mail import Mail
from flask_debugtoolbar import DebugToolbarExtension

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
