
from flask_script import Manager
from flask_script.commands import Command, ShowUrls, Option


class DBCreator(Command):
    def __init__(self):
        Command.__init__(self)
        self.add_option(Option('-d', '--drop',default=False, dest='drop'))

    def handle(self, f_app, *args, **kwargs):
        if kwargs.get("drop"):
            app_db.drop_all(app)

        app_db.create_all()


if __name__ == '__main__':

    from flask_migrate import MigrateCommand

    from os import environ
    environ.setdefault('EBC_CONFIG', "ebola.config.ConfigDev")

    from ebola import app, app_db

    manager = Manager(app)
    manager.add_command("schema", MigrateCommand)
    manager.add_command("create_db", DBCreator )
    manager.add_command("urls", ShowUrls)
    manager.run( default_command="runserver" )
