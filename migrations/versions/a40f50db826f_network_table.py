"""network table

Revision ID: a40f50db826f
Revises: 72a847cb2580
Create Date: 2020-05-06 02:31:37.498123

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a40f50db826f'
down_revision = '72a847cb2580'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('network',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('picture_name', sa.String(length=50), nullable=True),
    sa.Column('st_cat', sa.String(length=50), nullable=True),
    sa.Column('nd_cat', sa.String(length=50), nullable=True),
    sa.ForeignKeyConstraint(['picture_name'], ['news.picture'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('computer')
    op.create_unique_constraint(None, 'news', ['picture'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'news', type_='unique')
    op.create_table('computer',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('picture_name', sa.VARCHAR(length=50), nullable=True),
    sa.Column('st_cat', sa.VARCHAR(length=50), nullable=True),
    sa.Column('nd_cat', sa.VARCHAR(length=50), nullable=True),
    sa.ForeignKeyConstraint(['picture_name'], ['news.picture'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('network')
    # ### end Alembic commands ###
