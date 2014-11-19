from os import environ

DEBUG = True
TESTING = True
LOGIN_DISABLED = False

JSON_SORT_KEYS = False
JSONIFY_PRETTYPRINT_REGULAR = False

SQLALCHEMY_ECHO = True
SQLALCHEMY_POOL_SIZE = 20
SQLALCHEMY_DATABASE_URI = environ.get('EBOLA_CENTER_DB_URI', "postgresql://localhost/ebolacenter")

# SERVER_NAME = environ.get('EBOLA_CENTER_HOSTNAME', "localhost:5000")
SECRET_KEY = 'DontTellMom'



