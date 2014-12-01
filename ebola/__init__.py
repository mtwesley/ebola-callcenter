from flask import Flask, redirect, url_for
from flask.ext.login import LoginManager

from models import db, User
from views import views

import config


lm = LoginManager()

app = Flask(__name__, static_url_path='')
app.config.from_object(config)
app.config.from_envvar('EBOLACALLCENTER_CONFIG')
app.register_blueprint(views)

db.init_app(app)
lm.init_app(app)
lm.login_view = 'views.login'


@lm.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@lm.unauthorized_handler
def unauthorized():
    return redirect(url_for('views.login'))
