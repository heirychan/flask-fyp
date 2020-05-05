"""explosion by abc

Revision ID: 97ec5f118e3c
Revises: 307cbca27c21, 4a8e421db4c0, 537a79f1b75f, ae7a7b5a7b2a, bc64eeadc8d7, c6aa007a628e, c856aec3205b, ee0b5c39a592
Create Date: 2020-05-06 02:04:39.305864

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '97ec5f118e3c'
down_revision = ('307cbca27c21', '4a8e421db4c0', '537a79f1b75f', 'ae7a7b5a7b2a', 'bc64eeadc8d7', 'c6aa007a628e', 'c856aec3205b', 'ee0b5c39a592')
branch_labels = None
depends_on = None


def upgrade():
    pass


def downgrade():
    pass
