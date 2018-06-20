from flask import Flask
#from . import products


def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config.DevelopmentConfig')

    from flask_market.products.models import db, migrate
    db.init_app(app)
    migrate.init_app(app, db, 'migrations')

    # app.register_blueprint(products.products_app, url_prefix='/products')

    return app
