"""ads table

Revision ID: 155956eeda4c
Revises: f414549631fd
Create Date: 2020-05-07 03:04:00.319055

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '155956eeda4c'
down_revision = 'f414549631fd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ads',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('picture_name', sa.String(length=50), nullable=True),
    sa.Column('url', sa.String(length=9999), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_unique_constraint(None, 'news', ['picture'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'news', type_='unique')
    op.drop_table('ads')
    # ### end Alembic commands ###
