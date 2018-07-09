"""empty message

Revision ID: 171ba1730a52
Revises: a512aba6ba43
Create Date: 2018-07-09 15:24:55.603337

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '171ba1730a52'
down_revision = 'a512aba6ba43'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('media',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('path', sa.String(length=512), nullable=False),
    sa.Column('is_main', sa.Boolean(), server_default='0', nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['product_id'], ['market.products.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='market'
    )


def downgrade():
    op.drop_table('media', schema='market')
