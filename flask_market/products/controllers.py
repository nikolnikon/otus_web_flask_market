import json
from flask import render_template
from . import products_app
from flask_market.products.models import Product


@products_app.route('/')
def get_products_list():
    # todo Здесь было бы неплохо добавить пагинацию, но я уже видеть не могу этот магазин
    products = Product.query.all()
    return render_template('products/products_list.html', products=products)


@products_app.route('/<int:id>')
def get_product(id):
    product = Product.query.get_or_404(id)
    # Я не знаю, почему при запуске приложения под виндой поле Product.features стало строкой, а не словарем.
    # Под линуксом алхимия преобразует его в словарь.
    return render_template('products/product.html', product=product, features=json.loads(product.features))
