"""empty message

Revision ID: 0bbabc75dfa7
Revises: d661649ff990
Create Date: 2025-02-15 15:06:59.609627

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0bbabc75dfa7'
down_revision = 'd661649ff990'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.String(length=120), nullable=False))
        batch_op.create_unique_constraint(None, ['name'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('name')

    # ### end Alembic commands ###
