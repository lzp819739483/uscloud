from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)


from uscloud.host.views import host as hostModule
app.register_blueprint(hostModule)

