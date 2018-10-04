import os


class Config:
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'postgresql://postgres:12345678@localhost/flask_market')
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class ProductionConfig(Config):
    SECRET_KEY = os.getenv('SECRET_KEY', 'long_and_random_string')


class DevelopmentConfig(Config):
    SQLALCHEMY_ECHO = True
    TESTING = True
    SECRET_KEY = 'dev'
