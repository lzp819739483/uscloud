import os

from flask.ext.script import Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand

from uscloud import app, db
from uscloud.user.models import User
from uscloud.host.models import Host

Migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


def make_shell_context():
    return dict(app=app, db=db, User=User, Host=Host)


manager.add_command('shell', Shell(make_context=make_shell_context))


@manager.command
def initdb():
    """Init/reset database."""
    db.drop_all()
    db.create_all()
    admin = User(
        name=u'admin',
        password=u'123456',
        email='xx@qq.com',
        role=0,
        confirmed=True)
    demo = User(
        name=u'demo',
        password=u'123456',
        email=u'xy@qq.com',
        role=1,
        confirmed=True)
    db.session.add(admin)
    db.session.add(demo)
    db.session.commit()


if __name__ == '__main__':
    manager.run()
