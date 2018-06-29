from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_market.products.models import Product, Category, db

admin = Admin(name='flask_market_admin', template_mode='bootstrap3')
admin.add_view(ModelView(Product, db.session))
admin.add_view(ModelView(Category, db.session))
