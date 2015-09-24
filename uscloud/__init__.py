from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bootstrap import Bootstrap
from flask.ext.login import LoginManager


app = Flask(__name__)

app.config.from_object('config')

db = SQLAlchemy(app)

bootstrap = Bootstrap(app)

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'frontend.login'
login_manager.init_app(app)

from uscloud.host.views import host as hostModule
app.register_blueprint(hostModule)

from uscloud.user.views import user as userModule
app.register_blueprint(userModule)

from uscloud.frontend.views import frontend as frontendModule
app.register_blueprint(frontendModule)
