# config.py

import os
from settings import *

project_dir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False

class ConfigDevelopment(Config):
    DEBUG  = True
    SECRET_KEY = 'D_1OYtp2daiT1TNA4XroeQ'
    SQLALCHEMY_DB_URI = f'postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PW}@{POSTGRES_URL}/{POSTGRES_DB}'
    SQLALCHEMY_ENGINE_OPTIONS = {
        'echo': True,
    }

class ConfigTesting(Config):
    TESTING = True

class ConfigProduction(Config):
    pass

