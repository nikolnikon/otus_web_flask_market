from flask_admin import Admin, form
from flask_admin.contrib.sqla import ModelView
# from flask import url_for
# from jinja2 import Markup

from flask_market.products.models import Product, Category, Media, db


# class ImageView(ModelView):
#     def _list_thumbnail(view, context, model, name):
#         if not model.path:
#             return ''
#
#         return Markup('<img src="%s">' % url_for('static',
#                                                  filename=form.thumbgen_filename(model.path)))
#
#     column_formatters = {
#         'path': _list_thumbnail
#     }
#
#     # Alternative way to contribute field is to override it completely.
#     # In this case, Flask-Admin won't attempt to merge various parameters for the field.
#     form_extra_fields = {
#         'path': form.ImageUploadField('Media',
#                                       base_path='/static/images/products',
#                                       thumbnail_size=(100, 100, True))
#     }


admin = Admin(name='flask_market_admin', template_mode='bootstrap3')
admin.add_view(ModelView(Product, db.session))
admin.add_view(ModelView(Category, db.session))
admin.add_view(ModelView(Media, db.session))



