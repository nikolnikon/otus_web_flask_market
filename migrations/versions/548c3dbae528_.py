"""empty message

Revision ID: 548c3dbae528
Revises: 
Create Date: 2018-06-19 17:19:00.515232

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = '548c3dbae528'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.execute('create schema market')
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categories',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(length=256), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    schema='market'
                    )
    op.create_table('products',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(length=256), nullable=False),
                    sa.Column('description', sa.Text(), nullable=True),
                    sa.Column('features', postgresql.JSONB(none_as_null=True), nullable=True),
                    sa.Column('category_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['category_id'], ['market.categories.id'], ),
                    sa.PrimaryKeyConstraint('id'),
                    schema='market'
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('products', schema='market')
    op.drop_table('categories', schema='market')
    op.execute('drop schema market')
    # ### end Alembic commands ###
