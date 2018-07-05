from flask import render_template
from . import products_app
from flask_market.products.models import Product


@products_app.route('/')
def get_products_list():
    return render_template('products/products_list.html')


@products_app.route('/<int:id>')
def get_product(id):
    # if not id:
    #     # Запросить список товаров из БД
    #     # Отрендерить страницу со списком товаров
    #     pass
    # else:
    #     # Запросить из БД конкретный товар
    #     # Отрендерить страницу одного товара
    #     product = Product.query.get_or_404(id)
    #     # return render_template('products/product.htm', product=product)

    return render_template('products/product.html')
