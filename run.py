from ebola import app

if __name__ == '__main__':

    from flask_migrate import MigrateCommand
    from flask_script import Manager

    manager = Manager(app)
    manager.add_command("schema", MigrateCommand)
    manager.run( default_command="runserver")
