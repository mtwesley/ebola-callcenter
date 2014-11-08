
from datetime import date

# from gevent import monkey
# monkey.patch_all()
#
# from gevent_psycopg2 import monkey_patch
# monkey_patch()

import config

from flask.app import Flask, g
from flask_migrate import Migrate
from flask_session import Session

from db import app_db

app = Flask(__name__, static_url_path="/static")
app.config.from_object(config)

app_db.init_app(app)

Migrate(app, app_db)
Session(app)

# blueprints
from api import api
from ui import ui

app.register_blueprint(api)
app.register_blueprint(ui)

@app.before_request
def on_new_request():
    g.timestamp = date.today()


@app.route("/logout", endpoint="logout")
def logout_user():
    pass