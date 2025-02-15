"""empty message

Revision ID: c689059489c0
Revises: 38393452ab22
Create Date: 2025-02-15 17:43:55.498337

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c689059489c0'
down_revision = '38393452ab22'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('favorites',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('people_name', sa.String(length=120), nullable=False),
    sa.Column('planet_name', sa.String(length=120), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('people_id', sa.Integer(), nullable=True),
    sa.Column('planet_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['people_id'], ['people.id'], ),
    sa.ForeignKeyConstraint(['planet_id'], ['planet.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('prova')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('prova',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('climate', sa.VARCHAR(length=80), autoincrement=False, nullable=False),
    sa.Column('population', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('terrain', sa.VARCHAR(length=80), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='prova_pkey'),
    sa.UniqueConstraint('name', name='prova_name_key')
    )
    op.drop_table('favorites')
    # ### end Alembic commands ###
