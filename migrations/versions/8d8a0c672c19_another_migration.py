"""another migration

Revision ID: 8d8a0c672c19
Revises: 4f5b80751ff0
Create Date: 2024-02-06 19:39:44.389767

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8d8a0c672c19'
down_revision = '4f5b80751ff0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('car', schema=None) as batch_op:
        batch_op.drop_column('year')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('car', schema=None) as batch_op:
        batch_op.add_column(sa.Column('year', sa.INTEGER(), nullable=False))

    # ### end Alembic commands ###