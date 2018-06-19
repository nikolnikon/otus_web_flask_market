# todo Сделать загрузку параметров из файла или переменных окружения


class Config:
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:12345678@localhost/products'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = 'dev'


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True
