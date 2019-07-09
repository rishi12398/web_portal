"""empty message

Revision ID: 54aeacdbdb0d
Revises: c3bfce586f50
Create Date: 2019-07-08 16:45:39.613461

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '54aeacdbdb0d'
down_revision = 'c3bfce586f50'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('image_detail', sa.Column('name', sa.String(length=255), nullable=True))
    op.drop_column('image_detail', 'Name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('image_detail', sa.Column('Name', mysql.VARCHAR(length=255), nullable=True))
    op.drop_column('image_detail', 'name')
    # ### end Alembic commands ###