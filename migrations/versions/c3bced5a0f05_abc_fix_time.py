"""abc fix time

Revision ID: c3bced5a0f05
Revises: 467de01c9a43
Create Date: 2020-05-17 22:38:18.346605

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c3bced5a0f05'
down_revision = '467de01c9a43'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'news', ['picture'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'news', type_='unique')
    # ### end Alembic commands ###
