import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') or 'sqlite:///'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'localhost')
    MAIL_PORT = os.environ.get('MAIL_PORT', 8025)
    ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')
    SEARCH_INDEX_NAME = os.environ.get('SEARCH_INDEX_NAME')