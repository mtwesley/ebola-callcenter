from flask import Flask

app = Flask(__package__)

from . import db
