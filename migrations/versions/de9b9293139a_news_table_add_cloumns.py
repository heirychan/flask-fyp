"""news table add cloumns

Revision ID: de9b9293139a
Revises: 5bddd72a3012
Create Date: 2020-05-05 19:54:13.103873

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'de9b9293139a'
down_revision = '5bddd72a3012'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tech',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('picture_name', sa.String(length=50), nullable=True),
    sa.Column('st_cat', sa.String(length=50), nullable=True),
    sa.Column('nd_cat', sa.String(length=50), nullable=True),
    sa.ForeignKeyConstraint(['picture_name'], ['news.picture'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('news', sa.Column('picture', sa.String(length=50), nullable=True))
    op.add_column('news', sa.Column('time', sa.DateTime(), nullable=True))
    op.create_index(op.f('ix_news_time'), 'news', ['time'], unique=False)
    op.create_unique_constraint(None, 'news', ['picture'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'news', type_='unique')
    op.drop_index(op.f('ix_news_time'), table_name='news')
    op.drop_column('news', 'time')
    op.drop_column('news', 'picture')
    op.drop_table('tech')
    # ### end Alembic commands ###
