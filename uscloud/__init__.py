from flask import Flask

app = Flask(__name__)
app.config.from_object('config')


from uscloud.host.views import host as hostModule
app.register_blueprint(hostModule)

