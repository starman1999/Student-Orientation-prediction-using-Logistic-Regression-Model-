"""empty message

Revision ID: 006fc631e194
Revises: 49aa455dd812
Create Date: 2021-06-19 23:08:27.249830

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '006fc631e194'
down_revision = '49aa455dd812'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('moyennes', 'id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('moyennes', sa.Column('id', sa.INTEGER(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
