"""converting activities data to imperial and thus the need for Floats

Revision ID: d4b71349235c
Revises: bf8a9c23cab6
Create Date: 2023-05-09 11:08:20.812926

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd4b71349235c'
down_revision = 'bf8a9c23cab6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('activities', schema=None) as batch_op:
        batch_op.alter_column('distance',
               existing_type=sa.INTEGER(),
               type_=sa.Float(),
               existing_nullable=True)
        batch_op.alter_column('total_elevation_gain',
               existing_type=sa.INTEGER(),
               type_=sa.Float(),
               existing_nullable=True)
        batch_op.alter_column('elev_high',
               existing_type=sa.INTEGER(),
               type_=sa.Float(),
               existing_nullable=True)
        batch_op.alter_column('elev_low',
               existing_type=sa.INTEGER(),
               type_=sa.Float(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('activities', schema=None) as batch_op:
        batch_op.alter_column('elev_low',
               existing_type=sa.Float(),
               type_=sa.INTEGER(),
               existing_nullable=True)
        batch_op.alter_column('elev_high',
               existing_type=sa.Float(),
               type_=sa.INTEGER(),
               existing_nullable=True)
        batch_op.alter_column('total_elevation_gain',
               existing_type=sa.Float(),
               type_=sa.INTEGER(),
               existing_nullable=True)
        batch_op.alter_column('distance',
               existing_type=sa.Float(),
               type_=sa.INTEGER(),
               existing_nullable=True)

    # ### end Alembic commands ###
