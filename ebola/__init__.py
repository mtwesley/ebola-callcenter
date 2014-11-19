
import datetime

from flask import Flask, g

from models import db
from views import views

import config


app = Flask(__name__)
app.config.from_object(config)
app.register_blueprint(views)

db.init_app(app)

