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
    return render_template('products/product.html', product=product)
