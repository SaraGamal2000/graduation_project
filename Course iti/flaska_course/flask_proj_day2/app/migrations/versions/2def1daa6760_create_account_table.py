"""create account table

Revision ID: 2def1daa6760
Revises: b79f417373ee
Create Date: 2024-09-08 09:32:42.253114

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2def1daa6760'
down_revision = 'b79f417373ee'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('account',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=250), nullable=False),
    sa.Column('password', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('account')
    # ### end Alembic commands ###