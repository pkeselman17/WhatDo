import os

class Config:
    DEBUG = False
    DEVELOPMENT = False
    CONNECTION_STRING = ''

class DevelopmentConfig(Config):
    DEBUG = True
    DEVELOPMENT = True
    DB_NAME = 'plannerapp_dev'
    DB_HOST = 'localhost'
    DB_USER = os.environ['DB_USERNAME']
    DB_PASSWORD =os.environ['DB_PASSWORD']
    SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"