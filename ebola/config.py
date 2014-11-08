from os import environ

JSON_SORT_KEYS = False
JSONIFY_PRETTYPRINT_REGULAR = False
DEBUG = True
SQLALCHEMY_ECHO = True
SQLALCHEMY_POOL_SIZE = 20
SQLALCHEMY_DATABASE_URI = environ.get('EBOLA_CENTER_DB_URI', "postgresql://localhost/ebolacenter")
SERVER_NAME = environ.get('EBOLA_CENTER_HOSTNAME', "localhost:5000")
SESSION_TYPE = environ.get("session_type", 'filesystem')
SESSION_FILE_DIR = "/tmp/"



