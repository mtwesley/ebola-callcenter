from os import environ


class ConfigProduction:
    JSON_SORT_KEYS = False
    JSONIFY_PRETTYPRINT_REGULAR = False
    DEBUG = False
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_POOL_SIZE = 20
    SQLALCHEMY_DATABASE_URI = environ.get('EBOLA_CENTER_DB_URI', None)
    SERVER_NAME = environ.get('EBOLA_CENTER_HOSTNAME', None)


class ConfigDev(ConfigProduction):
    SQLALCHEMY_POOL_SIZE = 5
    SQLALCHEMY_ECHO = True
    DEBUG = True
    JSONIFY_PRETTYPRINT_REGULAR = True
    SERVER_NAME = "localhost:5000"
    SQLALCHEMY_DATABASE_URI = "postgresql://localhost/ebolacenter"