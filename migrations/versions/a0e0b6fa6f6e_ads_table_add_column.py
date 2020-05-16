"""ads table add column

Revision ID: a0e0b6fa6f6e
Revises: b81db0e4c59b
Create Date: 2020-05-16 20:27:08.958643

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a0e0b6fa6f6e'
down_revision = 'b81db0e4c59b'
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
