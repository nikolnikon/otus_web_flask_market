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
    features = db.Column(postgresql.JSONB(none_as_null=True))
    category_id = db.Column(db.Integer, db.ForeignKey('market.categories.id'), nullable=False)
    category = db.relationship('Category', backref=db.backref('products'), lazy=True)


class Category(db.Model):
    __table_args__ = {'schema': 'market'}
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False)
