"""news table try fix time..

Revision ID: b4a4b1778ae9
Revises: 1e1caf48fb78
Create Date: 2020-05-17 22:08:06.273209

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b4a4b1778ae9'
down_revision = '1e1caf48fb78'
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
