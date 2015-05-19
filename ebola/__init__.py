from flask import Flask, redirect, url_for, g, request, session, flash, render_template
from flask.ext.login import LoginManager, current_user

from models import db, User
from home import view as home
from admin import view as admin
from incoming import view as incoming
from outgoing import view as outgoing

import datetime
import config
import helpers


lm = LoginManager()

app = Flask(__name__)
app.config.from_object(config)
app.register_blueprint(home)
app.register_blueprint(admin)
app.register_blueprint(incoming)
app.register_blueprint(outgoing)

db.init_app(app)
lm.init_app(app)
lm.login_view = 'home.login'


@app.context_processor
def inject_helpers():
    return dict(helpers=helpers)


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


