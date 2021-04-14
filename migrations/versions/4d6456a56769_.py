"""empty message

Revision ID: 4d6456a56769
Revises: 50644d0f5a10
Create Date: 2021-04-10 22:45:09.552749

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4d6456a56769'
down_revision = '50644d0f5a10'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('fees',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fee_type', sa.String(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('amount', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('fees')
    # ### end Alembic commands ###