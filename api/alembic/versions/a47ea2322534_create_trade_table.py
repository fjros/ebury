"""create trade table

Revision ID: a47ea2322534
Revises: 
Create Date: 2020-01-26 23:10:45.253887

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a47ea2322534'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('trade',
                    sa.Column('id', sa.String(length=9), nullable=False),
                    sa.Column('sell_currency', sa.String(length=3), nullable=False),
                    sa.Column('sell_amount', sa.Integer(), nullable=False),
                    sa.Column('buy_currency', sa.String(length=3), nullable=False),
                    sa.Column('buy_amount', sa.Integer(), nullable=False),
                    sa.Column('rate', sa.Float(), nullable=False),
                    sa.Column('created_at', sa.DateTime(), nullable=False),
                    sa.PrimaryKeyConstraint('id'))


def downgrade():
    op.drop_table('trade')
