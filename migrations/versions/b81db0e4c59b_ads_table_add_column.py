"""ads table add column

Revision ID: b81db0e4c59b
Revises: 8d2989132d96
Create Date: 2020-05-16 03:00:38.931228

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b81db0e4c59b'
down_revision = '8d2989132d96'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('ads', sa.Column('big', sa.Boolean(), nullable=False))
    op.create_unique_constraint(None, 'news', ['picture'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'news', type_='unique')
    op.drop_column('ads', 'big')
    # ### end Alembic commands ###
