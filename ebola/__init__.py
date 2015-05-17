from flask import Flask, redirect, url_for, g, request, session, flash, render_template
from flask.ext.login import LoginManager, current_user

from models import db, User
from incoming import view as incoming
from home import view as home

import datetime
import config


lm = LoginManager()

app = Flask(__name__)
app.config.from_object(config)
app.register_blueprint(home)
app.register_blueprint(incoming)

db.init_app(app)
lm.init_app(app)
lm.login_view = 'home.login'


@lm.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@lm.unauthorized_handler
def unauthorized():
    return redirect(url_for('home.login'))


@app.before_request
def default_globals():
    g.timestamp = datetime.datetime.now()
    g.user = current_user


