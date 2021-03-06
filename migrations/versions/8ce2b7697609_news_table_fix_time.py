"""news table fix time

Revision ID: 8ce2b7697609
Revises: 52b433e902c5
Create Date: 2020-05-17 21:27:50.890421

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8ce2b7697609'
down_revision = '52b433e902c5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_news_time', table_name='news')
    op.create_unique_constraint(None, 'news', ['picture'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'news', type_='unique')
    op.create_index('ix_news_time', 'news', ['time'], unique=False)
    # ### end Alembic commands ###
