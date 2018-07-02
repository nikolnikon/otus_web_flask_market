"""Добавление поля price к таблице market.products

Revision ID: a512aba6ba43
Revises: 548c3dbae528
Create Date: 2018-07-02 16:12:26.178551

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'a512aba6ba43'
down_revision = '548c3dbae528'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('products', sa.Column('price', sa.Float, nullable=False), schema='market')


def downgrade():
    op.drop_column('market.products', 'price', schema='market')
