from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects import postgresql
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


class Product(db.Model):
    __table_args__ = {'schema': 'market'}
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    features = db.Column(postgresql.JSONB(none_as_null=True))
    category_id = db.Column(db.Integer, db.ForeignKey('market.categories.id'), nullable=False)

    category = db.relationship('Category', backref=db.backref('products'), lazy=True)
    photos = db.relationship('Media', backref=db.backref('product'))

    def __str__(self):
        return self.name


class Category(db.Model):
    __table_args__ = {'schema': 'market'}
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False)

    def __str__(self):
        return self.name


class Media(db.Model):
    __table_args__ = {'schema': 'market'}
    __tablename__ = 'media'
    id = db.Column(db.Integer, primary_key=True)
    path = db.Column(db.String(512), nullable=False)
    is_main = db.Column(db.Boolean, nullable=False, server_default='0')
    product_id = db.Column(db.Integer, db.ForeignKey('market.products.id'), nullable=False)

    def __str__(self):
        return 'Photo'
