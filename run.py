from ebola import app

if __name__ == '__main__':

    # from flask_migrate import MigrateCommand
    # from flask_script import Manager
    # from flask_script.commands import Command, ShowUrls, Option
    #
    # from os import environ
    # environ.setdefault('EBC_CONFIG', "config.py")

    app.run()

    # class DBCreator(Command):
    #     def __init__(self):
    #         Command.__init__(self)
    #
    #     def handle(self, f_app, *args, **kwargs):
    #         app_db.create_all()
    #
    # manager = Manager(app)
    # manager.add_command("schema", MigrateCommand)
    # manager.add_command("create_db", DBCreator )
    # manager.add_command("urls", ShowUrls)
    # manager.run( default_command="runserver" )
