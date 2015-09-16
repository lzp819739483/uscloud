import os

from flask.ext.script import Manager
from flask.ext.migrate import Migrate

from uscloud import app


manager = Manager(app)

if __name__ == '__main__':
    manager.run()


