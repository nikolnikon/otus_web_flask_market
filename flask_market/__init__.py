from flask import Flask
from .products import products_app
from .admin import admin


def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config.DevelopmentConfig')

    from flask_market.products.models import db, migrate
    db.init_app(app)
    migrate.init_app(app, db, 'migrations')

    admin.init_app(app)
    # admin.add_view()

    from flask_market.products import controllers
    app.register_blueprint(products_app, url_prefix='/products')

    from flask_market.fixtures import user_cli
    app.cli.add_command(user_cli)

    return app
