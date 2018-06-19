from flask import Blueprint

products_app = Blueprint('products_app', __name__)

@products_app.route('/')
def products_list():
    pass
