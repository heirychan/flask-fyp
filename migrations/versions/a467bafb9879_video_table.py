"""video table

Revision ID: a467bafb9879
Revises: 155956eeda4c
Create Date: 2020-05-07 03:32:24.976959

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a467bafb9879'
down_revision = '155956eeda4c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('video',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('picture_name', sa.String(length=50), nullable=True),
    sa.Column('st_cat', sa.String(length=50), nullable=True),
    sa.Column('vdo_link', sa.String(length=50), nullable=True),
    sa.ForeignKeyConstraint(['picture_name'], ['news.picture'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_unique_constraint(None, 'news', ['picture'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'news', type_='unique')
    op.drop_table('video')
    # ### end Alembic commands ###