"""editor table

Revision ID: 6003616cd15b
Revises: 52b433e902c5
Create Date: 2020-05-17 22:58:00.795134

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6003616cd15b'
down_revision = '52b433e902c5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('editor',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('picture_name', sa.String(length=50), nullable=True),
    sa.Column('st_cat', sa.String(length=50), nullable=True),
    sa.ForeignKeyConstraint(['picture_name'], ['news.picture'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_unique_constraint(None, 'news', ['picture'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'news', type_='unique')
    op.drop_table('editor')
    # ### end Alembic commands ###